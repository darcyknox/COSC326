/* regex.test() returns a boolean of if the input string
 * matches the regex it's being tested against
 */

function matchMailbox(str) {
  let re = new RegExp(/^[A-Z0-9]+([-_\.]?[A-Z0-9]+)*$/ig);

  return re.test(str);
}

// matchMailbox test cases
/*
console.log("Result 0 = ", matchMailbox("darcyKnox"));
console.log("Result 1 = ", matchMailbox("darcy-knox"));
console.log("Result 2 = ", matchMailbox("darcyknox_"));
console.log("Result 3 = ", matchMailbox("darcyknox123"));
console.log("Result 4 = ", matchMailbox("darcy-_knox"));
*/


/* At symbol */

function matchAt(str) {
  let re = new RegExp(/(@|_at_)/);

  return re.test(str);
}

// unnecessary comment

// matchAt test cases
/*
console.log("at result = ", matchAt('@'));
console.log("at result 1 = ", matchAt('_at_'));
console.log("at result 2 = ", matchAt('_at_@'));
console.log("at result 3 = ", matchAt('darcyknox'));
*/

/* Domain */

function matchDomain(str) {
  let re = new RegExp(/^([A-Z0-9]+((\.)?[A-Z0-9]+)*)+(\.|_dot_)$/ig); // not sure if I need the + before the final (\.|_dot_)

  return re.test(str);
}

// matchDomain test cases

/*
console.log(matchDomain('outlook.'));
console.log(matchDomain('outlook_dot_'));
console.log(matchDomain('outlook.mail.'));
console.log(matchDomain('outlook.tech_dot_'));
console.log(matchDomain('outlook_dot_tech_dot_'));
*/

function isNumericalDomain(str) {
  let re = new RegExp(/^\[([0-9]+((\.)?[0-9]+)*)\]/ig);

  return re.test(str);
}

function matchExt(str) {
  let re = new RegExp(/(co\.nz|com\.au|co\.uk|com|co\.us|co\.ca)$/ig);

  return re.test(str);
}

// matchExt test cases
/*
console.log(matchExt('darcy_knox@hotmail.co.nz'));
console.log(matchExt('outlook_dot_com'));
console.log(matchExt('outlook.co.nz'));
console.log(matchExt('outlook.com.au'));
console.log(matchExt('outlook.uk'));
*/

function matchDomainAndExt(str) {
  let re = new RegExp(/^([A-Z0-9]+((\.)?[A-Z0-9]+)*)+(\.|_dot_)(co\.nz|com\.au|co\.uk|com|co\.us|co\.ca)$/i);
  // g flag removed so that the regex can be tested twice
  // or test once and just return true
  // - either have g flag and return true
  // - or no g flag and return re.test(str)
  return re.test(str);
}

/*
console.log(matchDomainAndExt('outlook.com'));
console.log(matchDomainAndExt('outlook..com'));
*/

// FULL MATCH FUNCTION

function fullMatch(str) {
  let re = new RegExp(/^([A-Z0-9]+([-_\.]?[A-Z0-9]+)*)+(@|_at_)([A-Z0-9]+((\.)?[A-Z0-9]+)*)+(\.|_dot_)(co\.nz|com\.au|co\.uk|com|co\.us|co\.ca)$/ig);
  let error_message = "";

  if (re.test(str)) {
    // Replace all _at_ and _dot_ instances + convert to lowercase, nice.
    return str.replace(/_at_/, '@').replace(/_dot_/, '.').toLowerCase() + "\n";
    // or result = str.replace(/_at_/, '@').replace(/_dot_/, '.').toLowerCase() + "\n";
    // and return the string at the end with an empty error message
  } else { // there is an error unless the domain is in numerical form
    let splitted = str.split(/(@|_at_)/); // split at the @ symbol
    let mailbox = splitted[0];
    let atSymbol = splitted[1];
    let domainAndExt = splitted[2];
    if (!matchMailbox(mailbox)) { // if the mailbox doesn't match
      error_message += " <- Invalid mailbox";
    }
    if (!matchAt(str)) { // if there is no @ symbol in the whole string
      // console.log(atSymbol);
      error_message += " <- Missing @ symbol";
    } else { // if there is an @ symbol

      if (splitted.length > 3) {
        error_message += " <- Too many @ symbols"
      }
      // console.log(splitted[0], splitted[1], splitted[2]);
      /*
      if (!matchDomain(splitted[2])) { // if the domain doesn't match alphanumerically
        if (!isNumericalDomain(splitted[2])) { // if the domain doesn't match numerically
          error_message += " <- Invalid domain"; // print the error message if the domain is invalid for both domain formats
        }
      } else { // if the domain does match alphanumerically
        if (!matchExt(str)) {
          error_message += " <- Invalid extension";
        }
      }
      */
      if (!matchDomainAndExt(domainAndExt)) {
        let domainAndExtSplit = domainAndExt.split(/(co\.nz|com\.au|co\.uk|com|co\.us|co\.ca)/);
        let domain = domainAndExtSplit[0];
        let ext = domainAndExtSplit[1];
        //console.log(domain);
        //console.log(ext);
        if (!matchDomain(domain) && ext !== undefined) {
          if (!isNumericalDomain(domainAndExt)) {
            error_message += " <- Invalid domain";
          }
        } else {
          if (!matchExt(str) && !isNumericalDomain(domainAndExt)) {
            error_message += " <- Invalid extension";
          }
        }
      }
    }
  }
  // currently returns the accumulated issues unless an @ symbol is missing,
  // in which case, only the missing @ error messsage is returned
  return str + error_message + "\n";
}

// Need to find a place to split to test the inner parts - namely domain.
// Currently splits at the @ symbol if there is one.
// If there isn't, there should be a way to get at the domain from the back.
// If the domain is an ip/numerical address, the extension is not tested.
// The initial regex test will fail for numerical domains but will not print an error message


// FULL MATCH TESTING



console.log(fullMatch('darcy_knox@hotmail.co.nz'));
console.log(fullMatch('darcyknox_at_outlook_dot_com'));
console.log(fullMatch('darcy_knox@hotmail.com.nz'));
console.log(fullMatch('CEO@InsuroCorp.com'));
console.log(fullMatch('maffu@cs.otago.ac.nz'));
console.log(fullMatch('gerry_at_research.techies_dot_co.uk'));
console.log(fullMatch('bob@gmail..com'));
console.log(fullMatch('cath@[139.80.91.50]'));
console.log(fullMatch('b_at_g_dot_com'));
console.log(fullMatch('a-@gmail.com'));
console.log(fullMatch('BIG@@@'));
console.log(fullMatch('example.com'));
console.log(fullMatch('A@b@c@domain.com'));
console.log(fullMatch('abc”test”email@domain.com'));
console.log(fullMatch('abc is”not\valid@domain.com'));
console.log(fullMatch('.test@domain.com'));
console.log(fullMatch('test@domain..com'));
console.log(fullMatch(' darcyknox@outlook.com'));
console.log(fullMatch('darcyknox@outlook.com '));
console.log(fullMatch('plainaddress'));
console.log(fullMatch('#@%^%#$@#$@#.com'));
console.log(fullMatch('@example.com'));
console.log(fullMatch('Joe Smith <email@example.com>'));
console.log(fullMatch('email.example.com'));
console.log(fullMatch('email@example@example.com'));
console.log(fullMatch('.email@example.com'));
console.log(fullMatch('email.@example.com'));
console.log(fullMatch('email..email@example.com'));
console.log(fullMatch('あいうえお@example.com'));
console.log(fullMatch('email@example.com (Joe Smith)'));
console.log(fullMatch('email@example'));
console.log(fullMatch('email@-example.com'));
console.log(fullMatch('brad@lol.com'));
console.log(fullMatch('a_$b@cs.com'));
console.log(fullMatch('a___b@lol.com'));
console.log(fullMatch('a--b@cs.com'));
console.log(fullMatch('adsad.sdadsa@lol.com'));
console.log(fullMatch('a-b-c@l.com'));
console.log(fullMatch('ab_-l@a.com'));
console.log(fullMatch('la@l.com_'));
console.log(fullMatch('a_@l.com'));
console.log(fullMatch('123_123@lolc.com'));
console.log(fullMatch('a-$a@s.com'));
console.log(fullMatch('a_l@[123.123.123.123]'));
console.log(fullMatch('la.a@l.co.co.co.nz'));
console.log(fullMatch('mailbox@a.co.nz'));
console.log(fullMatch('mailbox@cs.co.uk'));
console.log(fullMatch('mailbox@l.co.uk'));
console.log(fullMatch('mail_box@domain.com'));
console.log(fullMatch('email_l@ex.l.com'));
