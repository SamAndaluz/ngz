odoo.define('openeducat_assignment_enterprise.tour', function (require) {
'use strict';

var tour = require("web_tour.tour");

tour.register('test_assignment_submit', {
    test: true,
    url: '/submited/assignment/list/1',
},
    [
        {
            content: "set BOA Sem-1-Asg-001",
            extra_trigger: '#name',
            trigger: 'span:contains(BOA Sem-1-Asg-001)',
        },
    ]
);

});