# Scanner-for-unauthenticated-jenkins
This scanner discovers for an given ip, port and protocol if the jenkins server is without authentication and therefore exploitable.

This tool is useful for the following:
Use Censys or Shodan to discover Server running jenkins.
Censys example query: https://censys.io/ipv4?q=80.http.get.title%3A+%22Dashboard%22+AND+%22Jenkins%22

Then you can run this script (automatically, if you use censys api) on every IP to determine which hosts are not password secured.
Then you can exploit further:
Further resources for exploiting: https://www.pentestgeek.com/penetration-testing/hacking-jenkins-servers-with-no-password
