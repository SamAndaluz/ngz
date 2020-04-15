odoo.define('openeducat_alumni_enterprise.tour', function (require) {
'use strict';

var tour = require("web_tour.tour");

tour.register('alumni_group', {
    test: true,
    url: '/alumni/detail/1',
},
    [
        {
            content: "select Sumita S Dani",
            extra_trigger: '#alumni',
            trigger: 'span:contains(Sumita)',
        },
    ]
);

});
