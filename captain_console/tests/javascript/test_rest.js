let chai = require('chai')


describe('Endpoint tests', () => {
    //###########################
    //These variables contain the ids of the existing event/booking
    //That way, you can use them in your tests (e.g., to get all bookings for an event)
    //###########################
    let eventId = '';
    let bookingId = '';

    //###########################
    //The beforeEach function makes sure that before each test, 
    //there is exactly one event and one booking (for the existing event).
    //The ids of both are stored in eventId and bookingId
    //###########################
    beforeEach((done) => {
        let event = new Event({ name: "Test Event", 
                                capacity: 10, 
                                startDate: 1590840000000, 
                                endDate: 1590854400000});

        Event.deleteMany({}, (err) => {
            Booking.deleteMany({}, (err) => {
                event.save((err, ev) => {
                    let booking = new Booking({ eventId: ev._id, 
                                                firstName: "Jane", 
                                                lastName: "Doe", 
                                                email: "jane@doe.com", 
                                                spots: 2 });
                    booking.save((err, book) => {
                        eventId = ev._id;
                        bookingId = book._id;
                        done();
                    });
                });
            });
        });
    });

    //###########################
    //Write your tests below here
    //###########################

    it("should always pass", function() {
        console.log("Our event has id " + eventId);
        console.log("Our booking has id " + bookingId);
        chai.expect(1).to.equal(1);
    });





    /********************************************
     * GET                                      *
     ********************************************/

    it("GET /events SUCCESS - all events", function(done) {
        chai.request('http://localhost:3000')
            .get('/api/v1/events')
            .set('Content-Type', 'appliction/json')
            .end( (err, res) => {
                chai.expect(res).to.have.status(200);
                chai.expect(res).to.be.json;
                chai.expect(typeof(res.body)).to.equal('object');
                chai.expect(res.body.length).to.equal(1);

                chai.expect(res.body[0]).to.haveOwnProperty('_id')
                chai.expect(res.body[0]).to.haveOwnProperty('name')
                chai.expect(res.body[0]).to.haveOwnProperty('capacity')
                chai.expect(res.body[0]).to.haveOwnProperty('startDate')
                chai.expect(res.body[0]).to.haveOwnProperty('endDate')
                chai.expect(res.body[0]).not.to.haveOwnProperty('location')
                chai.expect(res.body[0]).not.to.haveOwnProperty('description')

                chai.expect(typeof(res.body[0]._id)).to.equal('string')
                chai.expect(typeof(res.body[0].name)).to.equal('string')
                chai.expect(typeof(res.body[0].capacity)).to.equal('number')
                chai.expect(typeof(res.body[0].startDate)).to.equal('string')
                chai.expect(typeof(res.body[0].endDate)).to.equal('string')

                done();
        });
    });

});



