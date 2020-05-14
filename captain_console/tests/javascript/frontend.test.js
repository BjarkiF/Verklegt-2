let chai = require('chai')
let chaiHttp = require('chai-http')
let parseArguments = require('./chai-set-url')
chai.use(chaiHttp)

// TODO: log to a file

let url = parseArguments.url()
let creds = require('./creds').creds();

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
        /* Ná í forsíðuna. */
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


    it("GET / SUCCESS - Index", function(done) {
        /* Ná í forsíðuna. */
        chai.request(url)
            .get('/')
            .set('Content-Type', 'appliction/json')
            .end( (err, res) => {
                chai.expect(res).to.have.status(200);
                chai.expect(res).to.be.html;

                done();
        });
    });


    it("GET / SUCCESS - Index", function(done) {
        /* Ná í forsíðuna. */
        chai.request(url)
            .get('')
            .set('Content-Type', 'appliction/json')
            .end( (err, res) => {
                chai.expect(res).to.have.status(200);
                chai.expect(res).to.be.html;

                done();
        });
    });


    it("GET /cart/ SUCCESS", function(done) {
        /* Hvað gerist ef karfan er opnuð án þess að ská sig inn. */
 
        chai.request(url)
            .get('/cart/')
            .set('Content-Type', 'appliction/json')
            .end( (err, res) => {
                chai.expect(res).to.have.status(200);
                chai.expect(res).to.be.html;
                chai.expect(res.redirects[0]).to.equal(url + '/users/login?next=/cart/')
                chai.expect(typeof(res)).to.equal('object');

                done();
        });
    });


    it("GET /cart SUCCESS", function(done) {
        /* Hvað gerist ef karfan er opnuð án þess að ská sig inn. */
 
        chai.request(url)
            .get('/cart')
            .set('Content-Type', 'appliction/json')
            .end( (err, res) => {
                chai.expect(res).to.have.status(200);
                chai.expect(res).to.be.html;
                chai.expect(res.redirects[0]).to.equal(url + '/users/login?next=/cart/')
                chai.expect(typeof(res)).to.equal('object');

                done();
        });
    });


    it("GET /about/ SUCCESS", function(done) {
        /* Opna about */
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


    it("GET /about SUCCESS", function(done) {
        /* Opna about */
        chai.request(url)
            .get('/about')
            .set('Content-Type', 'appliction/json')
            .end( (err, res) => {
                chai.expect(res).to.have.status(200);
                chai.expect(res).to.be.html;

                /*chai.expect(typeof(res)).to.equal('object');*/

                done();
        });
    });


    it("GET /users/login/ SUCCESS", function(done) {
        chai.request(url)
            .get('/users/login')
            .set('Content-Type', 'appliction/json')
            .end( (err, res) => {
                chai.expect(res).to.have.status(200);
                chai.expect(res).to.be.html;
                //chai.expect(typeof(res)).to.equal('object');

                done();
        });
    });


    it("GET /login/ SUCCESS", function(done) {
        chai.request(url)
            .get('/login')
            .set('Content-Type', 'appliction/json')
            .end( (err, res) => {
                chai.expect(res).to.have.status(404);
                chai.expect(res).to.be.html;
                //chai.expect(typeof(res)).to.equal('object');

                done();
        });
    });


    it("GET /about/login SUCCESS", function(done) {
        chai.request(url)
            .get('/about/login')
            .set('Content-Type', 'appliction/json')
            .end( (err, res) => {
                chai.expect(res).to.have.status(404);
                chai.expect(res).to.be.html;
                //chai.expect(typeof(res)).to.equal('object');

                done();
        });
    });


    it("GET /about/login/ SUCCESS", function(done) {
        chai.request(url)
            .get('/about/login/')
            .set('Content-Type', 'appliction/json')
            .end( (err, res) => {
                chai.expect(res).to.have.status(404);
                chai.expect(res).to.be.html;
                //chai.expect(typeof(res)).to.equal('object');

                done();
        });
    });


    it("GET /items/login/ SUCCESS", function(done) {
        chai.request(url)
            .get('/items/login')
            .set('Content-Type', 'appliction/json')
            .end( (err, res) => {
                chai.expect(res).to.have.status(404);
                chai.expect(res).to.be.html;
                //chai.expect(typeof(res)).to.equal('object');

                done();
        });
    });


    it("GET /cart/login/ ERROR", function(done) {
        chai.request(url)
            .get('/cart/login')
            .set('Content-Type', 'appliction/json')
            .end( (err, res) => {
                chai.expect(res).to.have.status(404);
                chai.expect(res).to.be.html;
                //chai.expect(typeof(res)).to.equal('object');

                done();
        });
    });


    it("GET /management/login/ SUCCESS", function(done) {
        chai.request(url)
            .get('/management/login')
            .set('Content-Type', 'appliction/json')
            .end( (err, res) => {
                chai.expect(res).to.have.status(404);
                chai.expect(res).to.be.html;
                //chai.expect(typeof(res)).to.equal('object');

                done();
        });
    });

    
    it("GET /management/login/ SUCCESS creds superuser", function(done) {
        chai.request(url)
            .get('/management/login/')
            .auth(creds.superuser.username, creds.superuser.password)
            .set('Content-Type', 'appliction/json')
            .end( (err, res) => {
                chai.expect(res).to.have.status(404);
                chai.expect(res).to.be.html;
                //chai.expect(typeof(res)).to.equal('object');

                done();
        });
    });
    

    it("GET /management/groups FAIL invalid creds ", function(done) {
        chai.request(url)
            .get('/management/groups')
            .auth('notandi', 'eitthvaðbull')
            .set('Content-Type', 'appliction/json')
            .end( (err, res) => {
                chai.expect(res).to.have.status(200);
                chai.expect(res).to.be.html;
                //chai.expect(typeof(res)).to.equal('object');
                chai.expect(res.redirects[0]).to.equal(url + '/management/groups/')

                done();
        });
    });    


    it("GET /management/groups/ FAIL invalid creds ", function(done) {
        chai.request(url)
            .get('/management/groups/')
            .auth('notandi', 'eitthvaðbull')
            .set('Content-Type', 'appliction/json')
            .end( (err, res) => {
                chai.expect(res).to.have.status(200);
                chai.expect(res).to.be.html;
                //chai.expect(typeof(res)).to.equal('object');
                chai.expect(res.redirects[0]).to.equal(url + '/users/login?next=/management/groups/')

                done();
        });
    });

    //TODO: Gera fleiri frontend test.

    
});

