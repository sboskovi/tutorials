# Kafka
- Partition - queue
- partition key - opcionalan - odredjuje queue u koji se salje poruka. Ako se ne specificira onda je round robin npr
- Topic - logicki skup partition-a - vise partitiona sacinjava jedan topic
- Consumer Group - skup consumer-a koji citaju isti topic npr. Bitno da bi kafka pratila offset poslednje poruke koju su komitovali consumer-i
- Broker - server koji sadrzi topic-e?
- Kafka cluster - sadrzi vise brokera i radi leader / follower **replikaciju** da osigura **fault tolerance** i **durability**
- Leader / follower -  partition-i se repliciraju izmedju broker servera da bi osigurali fault tolerance
- Do **1MB** u porukama - ne stavljaj BLOB fajlove u message queue
- 1TB & 10k messages per second
- osnove **skaliranja** - izbrati dobar partition key da izbjegnes **hot partition**-e i skalirati brokere
- **confluent cloud** je managed kafka service - radi sam skaliranje, samo moras da izaberes partition key sam
- kako rijesiti hot partition:
  - Remove the key?
  - Compound key - event_id:partition_id npr - advertisement_id:1-10
  - uspori producer-a
- **Durability** podesavanja:
  - acks - koliko follower-a mora da potvrdi da su dobili poruku
  - replication factor - 3 is default
- vrlo vazno kada cosumeri commit-uju offset - tek kada consumer zavrsi posao

- batching - producer
- compressing - producer
- **idempotent** - da osiguramo da produceri posalju poruku jednom

- retention policy - milliseconds and bytes - 7 days and 16GB  