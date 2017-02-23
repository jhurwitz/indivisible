/**
 * Twilio Client configuration
 */

// Store some selectors for elements we'll reuse
var callStatus = $("#call-status");
var hangUpButton = $(".hangup-button");
var callCongresspersonButtons = $(".call-congressperson-button");

/* Helper function to update the call status bar */
function updateCallStatus(status) {
    callStatus.text(status);
}

/* Get a Twilio Client token with an AJAX request */
$(document).ready(function() {
    $.get("/members/token", {forPage: window.location.pathname}, function(data) {
        // Set up the Twilio Client Device with the token
        Twilio.Device.setup(data.token);
    });
});

/* Callback to let us know Twilio Client is ready */
Twilio.Device.ready(function (device) {
    updateCallStatus("Ready");
});

/* Report any errors to the call status display */
Twilio.Device.error(function (error) {
    updateCallStatus("ERROR: " + error.message);
});

/* Callback for when Twilio Client initiates a new connection */
Twilio.Device.connect(function (connection) {
    // Enable the hang up button and disable the call buttons
    hangUpButton.prop("disabled", false);
    callCongresspersonButtons.prop("disabled", true);

    updateCallStatus("In call with " + connection.message.phoneNumber);
});

/* Callback for when a call ends */
Twilio.Device.disconnect(function(connection) {
    // Disable the hangup button and enable the call buttons
    hangUpButton.prop("disabled", true);
    callCongresspersonButtons.prop("disabled", false);

    updateCallStatus("Ready");
});

/* Call a customer from a support ticket */
function callCongressperson(phoneNumber) {
    updateCallStatus("Calling " + phoneNumber + "...");

    var params = {"phoneNumber": phoneNumber};
    Twilio.Device.connect(params);
}

/* End a call */
function hangUp() {
    Twilio.Device.disconnectAll();
}