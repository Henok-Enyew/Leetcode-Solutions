/**
 * @param {string[]} details
 * @return {number}
 */
var countSeniors = function(details) {
     let counter = 0;
  details.forEach((element) => {
    if (element.slice(11, 13) > 60) counter++;
  });

  return counter;
};