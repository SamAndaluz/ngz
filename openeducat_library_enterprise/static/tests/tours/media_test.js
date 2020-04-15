odoo.define('openeducat_library_enterprise.tour', function (require) {
'use strict';

var tour = require("web_tour.tour");

tour.register('test_library', {
    test: true,
    url: '/library/media/1',
},
    [
        {
        content: "select Mathew James",
        extra_trigger: '#test1',
        trigger: 'span:contains(Mathew)',
        },
    ]
);

});