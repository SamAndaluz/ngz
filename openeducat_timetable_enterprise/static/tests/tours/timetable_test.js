odoo.define('openeducat_timetable_enterprise.tour', function (require) {
'use strict';

var tour = require("web_tour.tour");

tour.register('test_timetable', {
    test: true,
    url: '/student/timetable/1',
},
    [
        {
        content: "select James D church",
        extra_trigger: '#test',
        trigger: 'span:contains(James)',
        },
    ]
);

});