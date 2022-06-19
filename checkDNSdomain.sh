#!bash/bin
# author: Pawel Jurkiw
# email: 314275@uwr.edu.pl

domena=$1

echo "Domain: $domena";
dig $domena NS +short | sort -r | awk '{print "Name server: "$1;}';
dig $domena SOA +short | awk '$2 != "" {print "Hostmaster email: " $2;}';
dig $domena SOA +short | awk '$3 != "" {print "Last modification: " $3;}';
dig $domena MX +short | sort -n | awk '{print "Email server: " $1 " " $2;}';
