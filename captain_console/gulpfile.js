var gulp = require('gulp');
var sass = require('gulp-sass');
var watch = require('gulp-watch')
var concat = require('gulp-concat')
var csslint = require('gulp-csslint')
var sourcemaps = require('gulp-sourcemaps')
var htmlvalidator = require('html-validator')

/*
let files = {
  'library':{
    'js': [
        './bower_components/lodash/lodash.js',
        './bower_components/jquery/dist/jquery.min.js'
    ],
    'css':[
        './bower_components/bootstrap/dist/css/bootstrap.css',
        './bower_components/bootstrap/dist/css/bootstrap.css.map'
    ]
  }
}
*/

gulp.task('validatehtml', async function (done) {
    /* Check HTML Code for errors. */
      const options = {
          url: ['http://localhost:8000','http://localhost:8000/items/all/'],
          format: 'text',
          isLocal: true
      }

      try {
          const result = await htmlvalidator(options)
          console.log(result)
          return result
      } catch (error) {
          console.error(error)
          return 0
      }
});

gulp.task('clearstatic',function(done) {
    // rm -rf staticfiles/*
   require('child_process').spawn('rm', ['-rf', 'staticfiles/*'], { stdio: 'inherit' })(done);
});

gulp.task('collectstatic',function() {
    // python3 manage.py collectstatic
   require('child_process').spawn('python3', ['manage.py','collectstatic'], { stdio: 'inherit' });
});

gulp.task('scss', function(){
    /* Build the scss file. */
    return gulp.src('./static/scss/style.scss')
               .pipe(sass()) // Using gulp-sass
               .pipe(concat('style.css'))
               .pipe(csslint({
                    'shorthand': false
               }))
               .pipe(sourcemaps.write('.'))
               .pipe(csslint.formatter())
               .pipe(gulp.dest('./static/css/'))
});

/*
gulp.task('css-library', function(){
  return gulp.src(files.library.css)
    .pipe(gulp.dest('./static/css/lib'))
});

gulp.task('js-library', function(){
  return gulp.src(files.library.js)
    .pipe(gulp.dest('./static/js/lib'))
});
*/

gulp.task('watch', () => {
    gulp.watch('./static/scss/*.scss', function(done) {
        gulp.series(['scss'])(done);
    });
});

gulp.task('build', (done) => {
    gulp.series(['collectstatic', 'scss'])(done);
});

gulp.task('static', (done) => {
    gulp.series(['clearstatic', 'collectstatic'])(done);
});
