odoo.define('ibel_pos.WebClient', function (require) {

"use strict";

    var AbstractWebClient = require('web.AbstractWebClient');
    AbstractWebClient = AbstractWebClient.include({
    init: function() {
        this._super.apply(this, arguments);
        this.set('title_part', {"zopenerp": 'Ibel'});
    }
    });
});
