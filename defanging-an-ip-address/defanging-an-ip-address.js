/**
 * @param {string} address
 * @return {string}
 */
var defangIPaddr = function(address) {
    function replaceAll(string, search, replace) {
  return string.split(search).join(replace);
}
     const search = '.';
const replaceWith = '[.]';

const result = replaceAll(address, search, replaceWith);

return result

};