odoo.define('openeducat_online_admission.studnet_registration', function (require) {
    "use strict";
    var core = require('web.core');
    var Dialog = require("web.Dialog");
    var session = require('web.session');
    var ajax = require('web.ajax');
    var Widget = require('web.Widget');
    var websiteRootData = require('website.root');
    var utils = require('web.utils');
    var _t = core._t;
    var qweb = core.qweb;

    var StudentRegister = Widget.extend({
        events:{'change #self_application': '_onchangedropdown'},
        xmlDependencies: ['/openeducat_online_admission/static/src/xml/custome.xml'],
        init: function(){
            this._super.apply(this,arguments);
        },
        start: function () {
            return this._super();
        },
        _onchangedropdown: function(ev){
            var application = $(ev.currentTarget).val();
            ajax.jsonRpc('/get/application_data', 'call',
                {
                'application': application,
                }).then(function (data) {
                if (data['student_id'])
                {
                var student_data = qweb.render('GetStudentData',
                {
                    students: data['student_id'][0],
                    country: data['country_id']
                });
                $('.students').html(student_data);
                $('.country').html(student_data);
                }
                else if (data['country'])
                {
                  var others_data = qweb.render('GetOthersData',
                {
                    others: data['country'],
                });
                $('.others').html(others_data);
                }

            });
        }
    });

    websiteRootData.websiteRootRegistry.add(StudentRegister, '.js_get_data');
});