exports.url = () => {
    // Check if it's a valid url.
    function checkUrl(string) {
      try {
        new URL(string);
      } catch (_) {
        return false;
      }
      return true;
    }

    // Get the arguments.
    let argv = require('minimist')(process.argv.slice(2));
    let url = argv._[1];

    // If there is no url use 'localhost:8000'.
    if (!checkUrl(url)){
        url = 'http://localhost:8000'
    }

    console.log('Testing url: ' + url)

    return url
}
