const isPalindrome = function (s) {
  s = s.toLowerCase();
  let forward = "";
  let backward = "";
  for (let i = 0, j = s.length - 1; i < s.length, j >= 0; i++, j--) {
    if (isAlphanumeric(s[i])) forward = forward + s[i];
    if (isAlphanumeric(s[j])) backward = backward + s[j];
  }
  return forward === backward;
};

function isAlphanumeric(str) {
  return /^[0-9a-zA-Z]+$/.test(str);
}
