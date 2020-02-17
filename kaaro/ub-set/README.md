### Things for servers


#### When memory is bad
First you need to decide which partition you are interested in.

```
root@pc:~# df -h
Filesystem             Size  Used Avail Use% Mounted on
/dev/sda1               28G   26G  643M  98% /
none                   4.0K     0  4.0K   0% /sys/fs/cgroup
udev                   3.9G  4.0K  3.9G   1% /dev
tmpfs                  790M  1.5M  789M   1% /run
/dev/sda6              887G  685G  158G  82% /home
```

In my case I am interested in the / since it has 98% in use. In other words it is nearly full.

Now I use this command to see which files and directories contain the most bytes:

```
root@pc:~# du -ax / | sort -rn > /var/tmp/du-root-$(date --iso).log
```

Above command can take some time. If you are really unlucky the result is too big for /var/tmp. Then you need an other destination. Maybe a temporary mounted usb memory stick.


Finally see the results
```
root@pc:~# less /var/tmp/du-root-$(date --iso).log
```

Link from StackOverflow: https://askubuntu.com/questions/73160/how-do-i-find-the-amount-of-free-space-on-my-hard-drive/706532#706532?newreg=c911c17d96c7434a9f403f531e18fc87
