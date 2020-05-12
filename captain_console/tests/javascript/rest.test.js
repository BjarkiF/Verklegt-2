let chai = require('chai')
let chaiHttp = require('chai-http')
chai.use(chaiHttp)

let argv = require('minimist')(process.argv.slice(2));
let url = argv._[1];

function isValidUrl(string) {
  try {
    new URL(string);
  } catch (_) {
    return false;
  }

  return true;
}

if (isValidUrl(url)){
    console.log('Testing url: ' + url)
}else{
    url = 'http://localhost:8000'
}

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

    it("GET api/v1/items/all/ SUCCESS - all events", function(done) {
        chai.request(url)
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

    it("GET api/v1/cart/ SUCCESS - all events", function(done) {
        chai.request(url)
            .get('/api/v1/cart')
            .set('Content-Type', 'appliction/json')
            .end( (err, res) => {
                chai.expect(res).to.have.status(403);
                chai.expect(res).to.be.json;
                chai.expect(typeof(res)).to.equal('object');

                done();
        });
    });

    it("GET api/v1/users/ SUCCESS - all events", function(done) {
        chai.request(url)
            .get('/api/v1/users/')
            .set('Content-Type', 'appliction/json')
            .end( (err, res) => {
                chai.expect(res).to.have.status(403);
                chai.expect(res).to.be.json;
                chai.expect(typeof(res)).to.equal('object');

                done();
        });
    });

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
});

