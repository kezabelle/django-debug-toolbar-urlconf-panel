(function ($) {
    //var $namespaceFilter = $('#data-namespace');
    var $textFilter = $('#data-search');
    var rootSelector = '#urls-body > li'
    var tracking = {
        //namespace: '',
        text: ''
    }
    //var emptyNamespace = function() {
    //    var isEmpty = tracking.namespace === void(0) || tracking.namespace === null || tracking.namespace === '';
    //    return isEmpty;
    //}
    var emptyText = function() {
        var isEmpty = tracking.text === void(0) || tracking.text === null || $.trim(tracking.text) === '';
        return isEmpty;
    }

    var reset = function(event, val) {
        return $(rootSelector).removeAttr('disabled');
    };
    var filter = function(event, val) {
        var selectors = [];
        var selector = $(rootSelector);
        //var andFilters = [];
        //if (emptyNamespace() === false) {
        //    andFilters.push('[data-namespace="' + tracking.namespace + '"]');
        //}
        //var ands = andFilters.join("");
        //var finalSelector = selector.filter(ands);
        var orFilters = [];
        if (emptyText() === false) {
            parts = $.trim(tracking.text).toLowerCase().split(/\s+/);
            if (parts.length > 0) {
                $.each(parts, function (index, value) {
                    orFilters.push(rootSelector + '[data-text*="' + value + '"]');
                });
            }
        }
        if (orFilters.length > 0) {
            var finalFilters = orFilters.join(", ");
            var finalSelector = $(finalFilters);
            // disable all
            selector.attr('disabled','disabled');
        } else {
            var finalFilters = void(0);
            var finalSelector = selector;
        }
        // enable remaining.
        return finalSelector.removeAttr('disabled');
    };
    var applyFilters = function(event, lastVal) {
        if (emptyText() === true) {
            reset.call(this, event, lastVal);
        }
        return filter.call(this, event, lastVal);
    };


    //var namespaceChange = function(event) {
    //    var $t = $(this);
    //    var val = $t.val();
    //    if (tracking.namespace !== val) {
    //        tracking.namespace = val;
    //        applyFilters.call($t, event, val);
    //    }
    //}
    //$namespaceFilter.on('change', namespaceChange);

    var searchChange = function(event) {
        var $t = $(this);
        var val = $t.val();
        if (tracking.text !== val) {
            tracking.text = val;
            applyFilters.call($t, event, val);
        }
    };

    // avoid doing many many repaints if you're mid-typing-fast.
    var debounced = void(0);
    var searchChangeDebouncer = function(event) {
        if (debounced !== void(0)) {
            var cleared = clearTimeout(debounced);
        }
        var that = this;
        debounced = setTimeout(function() {
            return searchChange.call(that, event);
        }, 200);
        return debounced;
    };
    $textFilter.on('keyup', searchChangeDebouncer);
})(djdt.jQuery);
