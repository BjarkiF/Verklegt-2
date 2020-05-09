let chai = require('chai')
let chaiHttp = require('chai-http')
chai.use(chaiHttp)

describe('Endpoint tests', () => {
    //###########################
    //Write your tests below here
    //###########################

    it("should always pass", function() {
        //console.log("Our event has id " + eventId);
        //console.log("Our booking has id " + bookingId);
        chai.expect(1).to.equal(1);
    });

    /********************************************
     * GET                                      *
     ********************************************/

    it("GET /events SUCCESS - all events", function(done) {
        chai.request('https://captain-console-47.herokuapp.com')
            .get('/api/v1/items/all')
            .set('Content-Type', 'appliction/json')
            .end( (err, res) => {
                chai.expect(res).to.have.status(200);
                chai.expect(res).to.be.json;
                chai.expect(typeof(res)).to.equal('object');

                chai.expect(res.body).to.haveOwnProperty('count')
                chai.expect(res.body).to.haveOwnProperty('next')
                chai.expect(res.body).to.haveOwnProperty('previous')
                chai.expect(res.body).to.haveOwnProperty('results')

                chai.expect(typeof(res.body.count)).to.equal('number')
                chai.expect(typeof(res.body.next)).to.equal('string')
                chai.expect(typeof(res.body.previous)).to.equal('object')
                chai.expect(typeof(res.body.results)).to.equal('object')

                done();
        });
    });
});
