/** @odoo-module **/

import { WebClient } from "@web/webclient/webclient";
import { patch } from "@web/core/utils/patch";
import { session } from "@web/session";

patch(WebClient.prototype, "ibel_web.WebClient", {
    setup() {
        this._super.apply(this, arguments);
        this.title.setParts({ zopenerp: 'Ibel' }); // zopenerp is easy to grep
    }
});
