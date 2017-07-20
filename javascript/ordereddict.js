/**
 * Simple implementation of an ordered dictionary in JavaScript.
 */
function OrderedDict() {
    this.order = [];
    this.store = {};
}

OrderedDict.prototype.put = function (key, value) {
    if (!this.store.hasOwnProperty(key)) {
        this.order.push(key);
    }
    this.store[key] = value;
};

OrderedDict.prototype.get = function (key) {
    return this.store[key];
};

OrderedDict.prototype.getItems = function () {
    var store = this.store;
    return this.order.map(function (key) {
        return [key, store[key]];
    });
};
