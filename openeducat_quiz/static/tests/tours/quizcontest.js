odoo.define('openeducat_quiz.tour', function (require) {
'use strict';

var tour = require("web_tour.tour");

tour.register('quiz_test', {
    test: true,
    url: '/users/result-overview',
},
        [
            {
                content: "select There are currently no Result for your account",
                //extra_trigger: '#call',
                trigger: 'p:contains(There are currently no Result for your account)',
            },
        ]
);

});