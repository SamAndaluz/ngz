odoo.define('openeducat_alumni_blog_enterprise.tour', function (require) {
'use strict';

var tour = require("web_tour.tour");

tour.register('alumni_blog', {
    test: true,
    url: '/alumni/detail/1',
},
    [
        {
            content: "select Travel",
            extra_trigger: '#blog',
            trigger: 'span:contains(Travel)',
        },
    ]
);

});
