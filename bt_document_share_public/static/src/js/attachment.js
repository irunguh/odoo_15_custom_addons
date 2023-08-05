odoo.define('bt_document_share_public.AttachmentLink', function (require) {
"use strict";
var Widget = require('web.Widget');
var Chatter = require('mail.Chatter');
var AttachmentLink = Chatter.include({


    init: function () {
        	this._super.apply(this, arguments); 
		this.events = _.extend(this.events, {
        		'click .o_chatter_button_attachment_link': '_onClickAttachmentLinkButton',
        	});       	        	
    },	
        
    /*events: {
        'click .o_chatter_button_attachment_link': '_onClickAttachmentLinkButton',        
    },

    init: function () {
        this._super.apply(this, arguments); 		        	
    },	*/	    	    		
   _onClickAttachmentLinkButton: function () {
	console.log('gfgdch');
	console.log('zzzz');
	var self = this;	
	var context = {};
	if (self.context.default_model && self.context.default_res_id) {
        	context.active_model = self.context.default_model;
            	context.default_res_id = self.context.default_res_id;
            	context.active_id = self.context.default_res_id;
            }		
	var action = {
            type: 'ir.actions.act_window',
            name: "Attachment Link Wizard",
            res_model: 'attachment.link',
            view_mode: 'form',
            views: [[false, 'form']],
            target: 'new',
            context: context,
            
        };
        return this.do_action(action);
    },
});

return AttachmentLink;
});
