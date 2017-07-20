/**
 * Do an AJAX request to the passed URL. Retrieve it from a local cache
 * if the same request has been made before.
 */
var cachedAjax = (function () {
    var cache = {};
    return function (url) {
        if (cache.hasOwnProperty(url)) {
            return cache[url];
        }
        var data = $.ajax({
            url: url,
            async: false
        }).responseText;
        cache[url] = data;
        return data;
    }
})();
