var gulp = require('gulp');
var sass = require('gulp-sass');
var watch = require('gulp-watch')

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

gulp.task('scss', function(){
  return gulp.src('./scss/style.scss')
    .pipe(sass()) // Using gulp-sass
    .pipe(gulp.dest('./staticfiles/css'))
});

gulp.task('css-library', function(){
  return gulp.src(files.library.css)
    .pipe(gulp.dest('./staticfiles/css/lib'))
});

gulp.task('js-library', function(){
  return gulp.src(files.library.js)
    .pipe(gulp.dest('./staticfiles/js/lib'))
});

gulp.task('watch', () => {
    gulp.watch('scss/**/*.scss', (done) => {
        gulp.series(['scss'])(done);
    });
});
