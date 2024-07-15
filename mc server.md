 iptables -t nat -xvnL

tcpdump -i any 'tcp port 25565'


wg

wg-quick up wg0


### EC2 ubuntu
Pub key: sfN+GMjB+BR+5MJORW8h8odVFeWPDr62ybQuBEQ+8HI=

MC Ubuntu
Pub Key: 0GW1MmbG0CZQRyoaQ3azshq7Rhg7UbqZtv6yNn6+c14=



ssh -i "kaaroMCPem.pem" ubuntu@ec2-65-1-147-196.ap-south-1.compute.amazonaws.com

woodland mansion 10709 118 -790

End nether: 263 -14
End over world: tp karx01 2126 28 -36

---

```

# Allow traffic on specified ports
sudo iptables -A FORWARD -i eth0 -o wg0 -p tcp --syn --dport 80 -m conntrack --ctstate NEW -j ACCEPT
sudo iptables -A FORWARD -i eth0 -o wg0 -p tcp --syn --dport 443 -m conntrack --ctstate NEW -j ACCEPT

# Allow traffic between wg0 and eth0
sudo iptables -A FORWARD -i wg0 -o eth0 -m conntrack --ctstate ESTABLISHED,RELATED -j ACCEPT
sudo iptables -A FORWARD -i wg0 -o eth0 -m conntrack --ctstate ESTABLISHED,RELATED -j ACCEPT

# Forward traffic from eth0 to wg0 on specified ports
sudo iptables -t nat -A PREROUTING -i eth0 -p tcp --dport 80 -j DNAT --to-destination 192.168.4.2
sudo iptables -t nat -A PREROUTING -i eth0 -p tcp --dport 443 -j DNAT --to-destination 192.168.4.2

# Forward traffic back to eth0 from wg0 on specified ports
sudo iptables -t nat -A POSTROUTING -o wg0 -p tcp --dport 80 -d 192.168.4.2 -j SNAT --to-source 192.168.4.1
sudo iptables -t nat -A POSTROUTING -o wg0 -p tcp --dport 443 -d 192.168.4.2 -j SNAT --to-source 192.168.4.1
```