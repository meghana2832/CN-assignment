Group details -
1. 1KS17CS029 Harshitha V
2. 1KS17CS041 Meghana CV
3. 1KS17CS047 Nikita Katari

How the program work? 
Machine A sends ping request for 1 minute, takes a break for 30 seconds and again sends ping request for 1 minute to machine B. 
B implements rate limit using action "-j DROP" for A only and drops echo reply of 39 per minute and a burst rate of 14 per minute. 
When another machine sends a ping to machine B no packets are dropped. 

The ping packets receiving from that ip address 192.168.43.95 is being dropped at limit 39 per minite and burst rate is 14 per minute 

Challenges that we faced and how we over came them ?
we didnt know how to use -j DROP and -j ACCEPT commands. 
we approached our professor Ram sir for help and clarified our doubts and tried to solove the given question.

Contributions of Each team member -
this was a practical program exercise. therefore all the three of us sat down together to find out a solution.

What we learnt from this assignment-
we learnt how to iptables commands and to send ping packets from one machine to the other machine. Both the machines being two different operating systems.

