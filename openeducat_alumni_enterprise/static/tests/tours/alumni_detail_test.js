odoo.define('openeducat_alumni_enterprise.tour', function (require) {
'use strict';

var tour = require("web_tour.tour");

tour.register('alumni_detail', {
    test: true,
    url: '/alumni/detail/1',
},
    [
        {
            content: "select Global School",
            extra_trigger: '#alumni_detail',
            trigger: 'span:contains(Global)',
        },
    ]
);

});
