# sentry-cassandra-nodestorage

A [Lumanox, LLC](https://www.lumanox.com) Open Source project.

[Sentry](https://github.com/getsentry/sentry) extension implementing the
NodeStorage interface for Cassandra

## Installation

```bash
$ pip install sentry-cassandra-nodestore
```

## Configuration

```sql
CREATE KEYSPACE sentry WITH replication = {
  'class': 'SimpleStrategy',
  'replication_factor': '2'
};

USE sentry;

CREATE TABLE nodestore (
  key text PRIMARY KEY,
  flags int,
  value blob
) WITH
compaction={'sstable_size_in_mb': '160', 'class': 'LeveledCompactionStrategy'} AND
compression={'sstable_compression': 'SnappyCompressor'};
```

```python
SENTRY_NODESTORE = 'sentry-cassandra-nodestore.backend.CassandraNodeStorage'
SENTRY_NODESTORE_OPTIONS = {
    'servers': [
        '127.0.0.1:9042',
    ],
# (optional) specify an alternative keyspace
    'keyspace': 'sentry',
# (optional) specify an alternative columnfamily
    'columnfamily': 'nodestore',
}

```
