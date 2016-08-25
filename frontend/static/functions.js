$(document).ready(function () {

    // initialize search_history
    var search_state = new SearchState();
    search_state.init();

    // get the current search params (checked filters, date values, sort type and search query)
    var get_search_params = function (search_query_override) {
        var filters = {};
        filters['checkbox'] = {};
        filters['date'] = {};
        filters['sort'] = {};

        // set filters (checkboxes, dates, sort_type)
        $('.es_filter:checked').each(function () {
            var checkbox_elm = $(this);
            filters['checkbox'][checkbox_elm.attr('facet')] = checkbox_elm.attr('name');
        });
        filters['date']['created_on_start'] = $('#created_on_start').val();
        filters['date']['created_on_end'] = $('#created_on_end').val();
        filters['sort']['sort_type'] = $('.button--sort_by--active').val();

        if (search_query_override) {
            filters['search_query'] = search_query_override;
        } else {
            filters['search_query'] = $('#search_query').val();
        }

        return filters;
    };

    // submit search
    var submit_search = function () {
        var filters = get_search_params();

        $.ajax({
            url: '/reload',
            type: 'POST',
            data: JSON.stringify(filters),
            contentType: "application/json; charset=utf-8",
            success: function (data) {
                $("#reload-container").html(data);
                var history_data = search_state.init();
                $('#search_history').html(history_data);
                check_for_filters();
                open_facets();
            },
            error: function (error) {
                console.log('ERROR: ', error);
            }
        });

    };

    var open_facets = function () {
        $('.es_filter:checked').each(function () {
            var identifier = $(this).parent().prev().attr('id');
            $("#" + identifier).attr('checked', true);
            var arrow_id_part = $(this).parent().parent().attr('id');
            $('#arrow--' + arrow_id_part).removeClass('arrow--right').addClass('arrow--down').addClass('visible');
        });
    };


    // reset the checked filters and the date values
    var reset_filters = function () {
        $('.es_filter:checkbox').removeAttr('checked');
        // $('#created_on_start').val($.now().toString("dd.MM.yyyy"));
        var today = new Date();
        var end_date = ('0' + today.getDate()).slice(-2) + '.' + ('0' + (today.getMonth()+1)).slice(-2) + '.' + today.getFullYear();
        var start_date = ('0' + today.getDate()).slice(-2) + '.' + ('0' + (today.getMonth()-2)).slice(-2) + '.' + (today.getFullYear());
        $('#created_on_start').val(start_date);
        $('#created_on_end').val(end_date);
    };

    // if no filter is clicked, delete the reset all filters button
    var check_for_filters = function() {
        if (!$(".search_details__detail")[0]) {
            $('#reset_button').remove();
            $('.for').remove();
            $('.search_details').css('margin-bottom', 0);
        }
    };

    // get the previous search query
    var previous_search_query;
    $(document).on('focus', '#search_query', function () {
        previous_search_query = $('#search_query').val();
    });

    // click the submit button
    $(document).on('click', '#submit_button', function () {
        // reset current
        if(previous_search_query){
            search_state.save(get_search_params(previous_search_query));
            reset_filters();
        }
        submit_search();
    });

    // pressing enter in the searchbox
    $(document).on('keydown', '#search_query', function (e) {
        var key = e.which;
        if (key === 13) {
            if(previous_search_query){
                search_state.save(get_search_params(previous_search_query));
                reset_filters();
            }
            submit_search();
        }
    });

    // click on checkbox
    $(document).on('click', '.es_filter', function () {
        var facet = $(this).attr('facet');
        var test = $(this).parent().prev().attr('class');

        $(this).parent().prev().prop('checked', true);

        submit_search();
    });

    $(document).on('click', '.collapse', function () {
        console.log($(this));
        var open_facet = $(this).parent().parent().children(':first-child').attr('id');
        $('#' + open_facet).toggleClass("arrow--right arrow--down").show();
    });

    // date start field blur or enter
    $(document).on('blur', '#created_on_start', function () {
        submit_search();
    });
    $(document).on('keydown', '#created_on_start', function (e) {
        var key = e.which;
        if (key === 13) {
            submit_search();
        }
    });

    // date end field blur or enter
    $(document).on('blur', '#created_on_end', function () {
        submit_search();
    });
    $(document).on('keydown', '#created_on_end', function (e) {
        var key = e.which;
        if (key === 13) {
            submit_search();
        }
    });

    //type in searchbox, autocomplete
    $(document).on('keyup', '#search_query', function () {
        var value = $(this).val();
        $.ajax({
            url: '/autocomplete/' + value,
            type: 'POST',
            success: function (data) {
                $("#auto_complete_container").html(data);
            },
            error: function (error) {
                console.log(error);
            }
        });
    });

    //click on sort option
    $(document).on('click', '.button--sort_by', function () {
        var filters = get_search_params();
        filters['sort']['sort_type'] = $(this).val();

        var sort_type = $(this).val();
        $('.button--sort_by').removeClass('button--sort_by--active'); // remove all current selections
        $(this).addClass('button--sort_by--active');

        $.ajax({
            url: '/reload',
            type: 'POST',
            data: JSON.stringify(filters),
            contentType: "application/json; charset=utf-8",
            success: function (data) {
                $("#reload-container").html(data);
                var history_data = search_state.init();
                $('#search_history').html(history_data);
                check_for_filters();
                open_facets();

            },
            error: function (error) {
                console.log('ERROR: ', error);
            }
        });
    });

    // click the reset all filters button
    $(document).on('click', '#reset_button', function() {
        search_state.save(get_search_params());
        reset_filters();
        $('#search_query').val('');
        submit_search();
    });

    // click on a stored search in the search history
    $(document).on('click', '.stored_search', function() {
        var data = $(this).parent().attr("data-query");
        $.ajax({
            url: '/reload',
            type: 'POST',
            data: data,
            contentType: "application/json; charset=utf-8",
            success: function (data) {
                $("#reload-container").html(data);
                var history_data = search_state.init();
                $('#search_history').html(history_data);
                open_facets();

            },
            error: function (error) {
                console.log('ERROR: ', error);
            }
        });
    });

    // reset one filter
    $(document).on('click', '.button--reset_filter', function() {
        var facet = $(this).siblings().html();
        var facet_value = facet.substr(facet.indexOf(":") + 2);
        $('.es_filter[name="'+facet_value+'"]').prop( "checked", false );
        submit_search();
    });

    // reset search query
    $(document).on('click', '.button--reset_search_query', function() {
        $('#search_query').val('');
        submit_search();
    });

    // click in a suggestion on the no results page
    $(document).on('click', '.suggestion', function() {
        var search_query = $(this).text();
        $('#search_query').val(search_query);
        submit_search();
    });

    // open the link details of a link
    $(document).on('click', '.more_link_details', function() {
        var identifier = $(this).attr("id");
        $('#link_details_' + identifier).toggle();
        $('#arrow_down_' + identifier).toggle();
        $('#arrow_right_' + identifier).toggle();
        $('#more_details_' + identifier).toggle();
        $('#less_details_' + identifier).toggle();
    });

});
