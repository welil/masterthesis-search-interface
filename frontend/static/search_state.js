//manage search history
function SearchState() {

    var local_storage_key = 'search_history';

    // Object to persist (local storage)
    function Store() {
        this.searches = [];
        this.searches = JSON.parse(localStorage.getItem(local_storage_key)) || [];

        this.update = function (search) {
            this.searches.push(search);
            localStorage.setItem(local_storage_key, JSON.stringify(this.searches));
        };

        this.get = function() {
            return JSON.parse(localStorage.getItem(local_storage_key)) || [];
        }
    }

    // Search object to serialize the current state of search
    function Search(search_query, checkbox, date, sort) {
        this.search_query = search_query;
        this.checkbox = checkbox;
        this.date = date;
        this.sort = sort;
    }

    // instance variables
    this.store = new Store();

    // public functions

    // serialize and persist current search
    this.save = function (search_params) {
        var search = new Search(
            search_params.search_query, search_params.checkbox, search_params.date, search_params.sort);
        this.store.update(search);

        // show latest saved search
        this.init();
    };

    this.init = function () {
        var search_history_array = this.store.get();
        var array_length = search_history_array.length;
        $('#search_history').empty();
        for(var i=1; i<=3; i++){
            if(search_history_array[array_length-i]){
                var stored_search = search_history_array[array_length-i];
                // $('#search_history').append("<a href='#' class='stored_search' id='stored_search_" + i + "'>" + JSON.stringify(stored_search) + "</a><br/>");
                var search_string ='';
                if(stored_search.search_query){
                    search_string += "Searchquery: " + stored_search.search_query + ", ";
                }
                if(!jQuery.isEmptyObject(stored_search.checkbox)){
                    search_string += "Filters: ";
                }
                $.each(stored_search.checkbox, function(i) {
                    search_string += i + ": " + stored_search.checkbox[i] + ', ';
                });
                search_string += "From: " + stored_search.date.created_on_start + ", " + "To: " + stored_search.date.created_on_end + ", ";

                $('#search_history').append("<div class='test' data-query='" + JSON.stringify(stored_search) + "'>" +
                                                "<a href='#' title='" + search_string + "' class='stored_search'>" +  search_string + "</a>" +
                                            "</div>");
            }
        }
    }
}
