/*

 Script checks if there is an url parameter passed into the script.
 If not the url returned will be http://localhost:8000

*/


let checkUrl = (string) => {
    // Check if it's a valid url.
    try {
        new URL(string);
    } catch (_) {
        return false;
    }
return true;
}


let url = () => {
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

exports.url = url
