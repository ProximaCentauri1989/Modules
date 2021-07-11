# Modules

## grep

Input:

```python
python3 -m grep /home/docker/Documents/AWS/Connect/file.txt ssh
```
Output:

```python
Lines with 'ssh': ['ssh -i some.key ec2-user@13.13.13.13\n', 'ssh -i 1234.key ec2-user@16.16.16.16\n', 'Another line ssh -i 23456.key ec2-user@17.16.16.16\n']
```

## sed

Input:

```python
python3 -m sed /home/docker/Documents/AWS/Connect/file.txt "ssh/ftp"
```

## jq

Input:

```python
python3 -m jq /home/docker/Documents/AWS/Connect/file.json '/second'
```

Output:
```python
Found the next element: {'latitude': 10.2333, 'longitude': 123.2332}
```

