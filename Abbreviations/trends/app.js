
const googleTrends = require('google-trends-api');

const allTopics= ['AWS','S3','GCP','GCLB','Amazon ES','AMI','ARN','EC2','ECS','EFS','EMR','IaaS','SWS','SNS','GCS','VPC','Amazon EBS','AZ','ASG','EBS','ELB','EIP','ENI','FaaS','HPC','HVM','S3 IA','IG','KMS','Amazon SES','RRS','SQS','TPM','VPG','VPS','HP CSA','SEO','SCM','SEM','WP','PPC','CPC','SERP','CTS','CR','CPM','SVG','DMCA','CMS','CRO','CTA','CTR','PR','DA','ROI','UI/UX','SEA','SMO','SMM','SERM','AMA','B2B','B2C','CRM','CX','FOMO','GA','IO','SM','SMP','ToS','UA','CPL','NPS','QDD','QDF','SC','ZMOT','HITS','LSI','PBN','IMS','ML','NI','MI','NLP','CNN','RNN','LSTM','CTC','CV','HMD','RL','NLNN','SR','M2M','DSBS','LNN','NLU','RPA','ANN','SQL','DQL','DDL','DML','RDSMS','OLAP','OLTP','DRDA','4D QL','DMS','FIFO','PHP','HTML','JS','CSS','SaaS','API','XML','SOAP','XHTML','JSON','EOF','SDK','ASCII','I/0','WYSIWYG','VCS','IDE','Java EE','EOL','XSD','VBS','RAD','JCE','JDK','IPSec','SSE','SSL','TLS','DOS','DDoS','XSS','CSP','CSRF','SQLi','CBSP','ACL','AES','CORS','IAM','MFA','WAF','OWASP','MITM','PCI DSS','SAML','STS','FUD','RAT','SE','SKid','DNSSEC','DKIM','DMARC','SPF','CVSS','SAST','DAST','WAP','RFI','LFI','DT','PT','SCD','OSCI','CWE','DSA','OSS','FOSS','OS','HA','BYOD','PaaS','DaaS','VM','KVM','ESX','DRS','VSM','QEMU','SSD','IOPS','ADFS','CLI','CI/CD','iSCSI','SSH','MSTSC','MPP','NFS','RAID','RAM','SLA','OLA','SSO','VTL','VDI','BIOS','DVD','PSU','ROM','UPS','DC','GUI','TPU','RISC','AU','ALU','AVX','P2V','VXLAN','VCS','HAC','RUM','ERP','BPO','BI','IT','DW','WINS','WMI','VG','TTY','SFTP','DNS','HTTP','HTTPS','CDN','LAN','WAN','DHCP','TCP','IP','WWW','IoT','D2D','VPN','BGP','VLAN','DOM','UDP','CIDR','VIP','ICMP','LB','SMTP','FTP','RDP','MPLS','NS','NAT','SOA','TTL','TPS','NDA','AP','MAC','NIC','ISP','URL','PDF','TLD','RSS','IFTTT','IE','AFAIK','CAN-SPAM','DM','FB','PM','QoS','MIME','POP','IMAP','CNAME','MX','PPTP','LLT','POP (CDN)','ASN','SCM (Commerce)','WPAN','WLAN','URI','TTF','NACK','HAR','lastELEMENT'];
let dataToSet = [];
for(let i=0;i < allTopics.length; i++) {
// allTopics.forEach( topic => {
  let topic = allTopics[i];
  let topics = ['AI',topic];
  if (topic === 'lastELEMENT') {
    console.log(dataToSet);
  }
  googleTrends.interestOverTime({ keyword: topics })
    .then(function (results) {
      const resultObj = JSON.parse(results);
      // console.log(resultObj.default.averages);
      avgs = resultObj.default.averages;
      const objToPush = {
        topic: topic,
        value: avgs[1]/avgs[0]
      };
      dataToSet.push(objToPush);
      // console.log(objToPush);
      // console.log(Object.keys(resultObj));
      console.log(dataToSet);
    })
    .catch(function (err) {
      console.error('Oh no there was an error', err);
    });
  
}
console.log(dataToSet);



