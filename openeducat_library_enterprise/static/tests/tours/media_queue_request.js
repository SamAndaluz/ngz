odoo.define('openeducat_library_enterprise.tour', function (require) {
'use strict';

var tour = require("web_tour.tour");

tour.register('test_media_queue_request', {
    test: true,
    url: '/media/queue/request',
},
    [
        {
        content: "add Troposhere In Detail",
        trigger: 'form[action^="/queue/request/submit"]',
        },
    ]
);

});