odoo.define('ibel.UserMenu', function (require) {
    "use strict";

    /**
     * This widget is appended by the webclient to the right of the navbar.

     * If clicked, it opens a dropdown allowing the user to perform actions like
     * editing its preferences, accessing the documentation, logging out...
     */

    var UserMenu = require('web.UserMenu');
    var documentation_url = 'https://docs.ibel.app/14.0/applications.html';
    var support_url = 'https://ibeltechnology.com/help';

    UserMenu.include({
        init: function () {
            this._super.apply(this, arguments);
            var self = this;
            var session = this.getSession();
            var lang_list = '';

            self._rpc({
                model: 'ir.config_parameter',
                method: 'search_read',
                domain: [['key', '=like', 'app_%']],
                fields: ['key', 'value'],
                lazy: false,
            }).then(function (res) {
                $.each(res, function (key, val) {
                    if (val.key == 'app_documentation_url')
                        documentation_url = val.value;
                    if (val.key == 'app_support_url')
                        support_url = val.value;
                });
            })
        },  
        
        _onMenuDocumentation: function () {
            window.open(documentation_url, '_blank');
        },
        _onMenuSupport: function () {
            window.open(support_url, '_blank');
        },      
       
    })

});
