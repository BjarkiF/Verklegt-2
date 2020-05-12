let chai = require('chai')
let chaiHttp = require('chai-http')
chai.use(chaiHttp)

// Get the arguments.
let argv = require('minimist')(process.argv.slice(2));
let url = argv._[1];

// Check if it's a valid url.
function isValidUrl(string) {
  try {
    new URL(string);
  } catch (_) {
    return false;
  }
  return true;
}

// If there is no url use 'localhost:8000'.
if (!isValidUrl(url)){
    url = 'http://localhost:8000'
}

console.log('Testing url: ' + url)

describe('Endpoint tests', () => {
    //###########################
    //Write your tests below here
    //###########################

    it("should always pass", function() {
        chai.expect(1).to.equal(1);
    });

    /********************************************
     * GET                                      *
     ********************************************/

    it("GET / SUCCESS - Index", function(done) {
        chai.request(url)
            .get('/')
            .set('Content-Type', 'appliction/json')
            .end( (err, res) => {
                chai.expect(res).to.have.status(200);
                chai.expect(res).to.be.html;
                /*
                chai.expect(typeof(res)).to.equal('object');

                chai.expect(res.body).to.haveOwnProperty('count')
                chai.expect(res.body).to.haveOwnProperty('next')
                chai.expect(res.body).to.haveOwnProperty('previous')
                chai.expect(res.body).to.haveOwnProperty('results')

                chai.expect(typeof(res.body.count)).to.equal('number')
                chai.expect(typeof(res.body.next)).to.equal('string')
                chai.expect(typeof(res.body.previous)).to.equal('object')
                chai.expect(typeof(res.body.results)).to.equal('object')
                */
                done();
        });
    });

    it("GET /cart/ SUCCESS - all events", function(done) {
        /*
        TODO: laga /cart/ routing þegar notandi er ekki innskráður.
        */
        chai.request(url)
            .get('/cart/')
            .set('Content-Type', 'appliction/json')
            .end( (err, res) => {
                chai.expect(res).to.have.status(403);
                chai.expect(res).to.be.html;
                //chai.expect(typeof(res)).to.equal('object');

                done();
        });
    });

    it("GET /about/ SUCCESS - all events", function(done) {
        chai.request(url)
            .get('/about/')
            .set('Content-Type', 'appliction/json')
            .end( (err, res) => {
                chai.expect(res).to.have.status(200);
                chai.expect(res).to.be.html;

                /*chai.expect(typeof(res)).to.equal('object');*/

                done();
        });
    });
    /*
    it("GET api/v1/user/1337/ SUCCESS - all events", function(done) {
        chai.request(url)
            .get('/api/v1/user/1337/')
            .set('Content-Type', 'appliction/json')
            .end( (err, res) => {
                chai.expect(res).to.have.status(403);
                chai.expect(res).to.be.json;
                chai.expect(typeof(res)).to.equal('object');

                done();
        });
    });
    */
});
