
## Querying Ensembl

```sh
> brew install mysql
> mysql -u anonymous -h ensembldb.ensembl.org -P 3306
```

## Assignment 1

> How many databases are available for cat, felis catus?

```sh
mysql> show databases like 'felis%';
```

```sh
+---------------------------------+
| Database (felis%)               |
+---------------------------------+
| felis_catus_core_48_1c          |
| felis_catus_core_49_1c          |
| felis_catus_core_50_1d          |
| felis_catus_core_51_1e          |
| felis_catus_core_52_1f          |
| felis_catus_core_53_1f          |
| felis_catus_core_54_1f          |
| felis_catus_core_55_1f          |
| felis_catus_core_56_1f          |
| felis_catus_core_57_1f          |
| felis_catus_core_58_1g          |
| felis_catus_core_59_1h          |
| felis_catus_core_60_1i          |
| felis_catus_core_61_1j          |
| felis_catus_core_62_1k          |
| felis_catus_core_63_1           |
| felis_catus_core_64_1           |
| felis_catus_core_65_1           |
| felis_catus_core_66_1           |
| felis_catus_core_67_1           |
| felis_catus_core_68_1           |
| felis_catus_core_69_1           |
| felis_catus_core_70_62          |
| felis_catus_core_71_62          |
| felis_catus_core_72_62          |
| felis_catus_core_73_62          |
| felis_catus_core_74_62          |
| felis_catus_core_75_62          |
| felis_catus_core_76_62          |
| felis_catus_core_77_62          |
| felis_catus_core_78_62          |
| felis_catus_core_79_62          |
| felis_catus_core_80_62          |
| felis_catus_core_81_62          |
| felis_catus_core_82_62          |
| felis_catus_core_83_62          |
| felis_catus_core_84_62          |
| felis_catus_core_85_62          |
| felis_catus_core_86_62          |
| felis_catus_core_87_62          |
| felis_catus_core_88_62          |
| felis_catus_core_89_62          |
| felis_catus_core_90_62          |
| felis_catus_core_91_8           |
| felis_catus_core_92_8           |
| felis_catus_core_93_9           |
| felis_catus_core_94_9           |
| felis_catus_core_95_9           |
| felis_catus_funcgen_92_8        |
| felis_catus_funcgen_93_9        |
| felis_catus_funcgen_94_9        |
| felis_catus_funcgen_95_9        |
| felis_catus_otherfeatures_70_62 |
| felis_catus_otherfeatures_71_62 |
| felis_catus_otherfeatures_72_62 |
| felis_catus_otherfeatures_73_62 |
| felis_catus_otherfeatures_74_62 |
| felis_catus_otherfeatures_75_62 |
| felis_catus_otherfeatures_76_62 |
| felis_catus_otherfeatures_77_62 |
| felis_catus_otherfeatures_78_62 |
| felis_catus_otherfeatures_79_62 |
| felis_catus_otherfeatures_80_62 |
| felis_catus_otherfeatures_81_62 |
| felis_catus_otherfeatures_82_62 |
| felis_catus_otherfeatures_83_62 |
| felis_catus_otherfeatures_84_62 |
| felis_catus_otherfeatures_85_62 |
| felis_catus_otherfeatures_86_62 |
| felis_catus_otherfeatures_87_62 |
| felis_catus_otherfeatures_88_62 |
| felis_catus_otherfeatures_89_62 |
| felis_catus_otherfeatures_90_62 |
| felis_catus_otherfeatures_91_8  |
| felis_catus_otherfeatures_92_8  |
| felis_catus_otherfeatures_93_9  |
| felis_catus_otherfeatures_94_9  |
| felis_catus_otherfeatures_95_9  |
| felis_catus_rnaseq_70_62        |
| felis_catus_rnaseq_71_62        |
| felis_catus_rnaseq_72_62        |
| felis_catus_rnaseq_73_62        |
| felis_catus_rnaseq_74_62        |
| felis_catus_rnaseq_75_62        |
| felis_catus_rnaseq_76_62        |
| felis_catus_rnaseq_77_62        |
| felis_catus_rnaseq_78_62        |
| felis_catus_rnaseq_79_62        |
| felis_catus_rnaseq_80_62        |
| felis_catus_rnaseq_81_62        |
| felis_catus_rnaseq_82_62        |
| felis_catus_rnaseq_83_62        |
| felis_catus_rnaseq_84_62        |
| felis_catus_rnaseq_85_62        |
| felis_catus_rnaseq_86_62        |
| felis_catus_rnaseq_87_62        |
| felis_catus_rnaseq_88_62        |
| felis_catus_rnaseq_89_62        |
| felis_catus_rnaseq_90_62        |
| felis_catus_rnaseq_91_8         |
| felis_catus_rnaseq_92_8         |
| felis_catus_rnaseq_93_9         |
| felis_catus_rnaseq_94_9         |
| felis_catus_rnaseq_95_9         |
| felis_catus_variation_61_1j     |
| felis_catus_variation_62_1k     |
| felis_catus_variation_63_1      |
| felis_catus_variation_64_1      |
| felis_catus_variation_65_1      |
| felis_catus_variation_66_1      |
| felis_catus_variation_67_1      |
| felis_catus_variation_68_1      |
| felis_catus_variation_69_1      |
| felis_catus_variation_70_62     |
| felis_catus_variation_71_62     |
| felis_catus_variation_72_62     |
| felis_catus_variation_73_62     |
| felis_catus_variation_74_62     |
| felis_catus_variation_75_62     |
| felis_catus_variation_76_62     |
| felis_catus_variation_77_62     |
| felis_catus_variation_78_62     |
| felis_catus_variation_79_62     |
| felis_catus_variation_80_62     |
| felis_catus_variation_81_62     |
| felis_catus_variation_82_62     |
| felis_catus_variation_83_62     |
| felis_catus_variation_84_62     |
| felis_catus_variation_85_62     |
| felis_catus_variation_86_62     |
| felis_catus_variation_87_62     |
| felis_catus_variation_88_62     |
| felis_catus_variation_89_62     |
| felis_catus_variation_90_62     |
| felis_catus_variation_91_8      |
| felis_catus_variation_92_8      |
| felis_catus_variation_93_9      |
| felis_catus_variation_94_9      |
| felis_catus_variation_95_9      |
+---------------------------------+
139 rows in set (0.09 sec)
```
## Assignment 2
> Use the show and describe commands to figure:
* what tables are related to describing genes, transcripts, and exons. 
* What information are these tables storing
* how do the tables relate to each other?

### Genes:

```sh
mysql> show tables like '%gene%';
```

```sh
mysql> describe gene;
```

```sh
+-------------------------+----------------------+------+-----+---------+----------------+
| Field                   | Type                 | Null | Key | Default | Extra          |
+-------------------------+----------------------+------+-----+---------+----------------+
| gene_id                 | int(10) unsigned     | NO   | PRI | NULL    | auto_increment |
| biotype                 | varchar(40)          | NO   |     | NULL    |                |
| analysis_id             | smallint(5) unsigned | NO   | MUL | NULL    |                |
| seq_region_id           | int(10) unsigned     | NO   | MUL | NULL    |                |
| seq_region_start        | int(10) unsigned     | NO   |     | NULL    |                |
| seq_region_end          | int(10) unsigned     | NO   |     | NULL    |                |
| seq_region_strand       | tinyint(2)           | NO   |     | NULL    |                |
| display_xref_id         | int(10) unsigned     | YES  | MUL | NULL    |                |
| source                  | varchar(40)          | NO   |     | NULL    |                |
| description             | text                 | YES  |     | NULL    |                |
| is_current              | tinyint(1)           | NO   |     | 1       |                |
| canonical_transcript_id | int(10) unsigned     | NO   | MUL | NULL    |                |
| stable_id               | varchar(128)         | YES  | MUL | NULL    |                |
| version                 | smallint(5) unsigned | YES  |     | NULL    |                |
| created_date            | datetime             | YES  |     | NULL    |                |
| modified_date           | datetime             | YES  |     | NULL    |                |
+-------------------------+----------------------+------+-----+---------+----------------+
16 rows in set (0.06 sec)
```

### Transcripts:

```sh
mysql> show tables like '%transcript%';
```

```sh
mysql> describe transcript;
```

```sh
+--------------------------+----------------------+------+-----+---------+----------------+
| Field                    | Type                 | Null | Key | Default | Extra          |
+--------------------------+----------------------+------+-----+---------+----------------+
| transcript_id            | int(10) unsigned     | NO   | PRI | NULL    | auto_increment |
| gene_id                  | int(10) unsigned     | YES  | MUL | NULL    |                |
| analysis_id              | smallint(5) unsigned | NO   | MUL | NULL    |                |
| seq_region_id            | int(10) unsigned     | NO   | MUL | NULL    |                |
| seq_region_start         | int(10) unsigned     | NO   |     | NULL    |                |
| seq_region_end           | int(10) unsigned     | NO   |     | NULL    |                |
| seq_region_strand        | tinyint(2)           | NO   |     | NULL    |                |
| display_xref_id          | int(10) unsigned     | YES  | MUL | NULL    |                |
| source                   | varchar(40)          | NO   |     | ensembl |                |
| biotype                  | varchar(40)          | NO   |     | NULL    |                |
| description              | text                 | YES  |     | NULL    |                |
| is_current               | tinyint(1)           | NO   |     | 1       |                |
| canonical_translation_id | int(10) unsigned     | YES  | UNI | NULL    |                |
| stable_id                | varchar(128)         | YES  | MUL | NULL    |                |
| version                  | smallint(5) unsigned | YES  |     | NULL    |                |
| created_date             | datetime             | YES  |     | NULL    |                |
| modified_date            | datetime             | YES  |     | NULL    |                |
+--------------------------+----------------------+------+-----+---------+----------------+
```

### Exons:

```sh
mysql> show tables like '%exon%';
```

```sh
mysql> describe exon;
```

```sh
+-------------------+----------------------+------+-----+---------+----------------+
| Field             | Type                 | Null | Key | Default | Extra          |
+-------------------+----------------------+------+-----+---------+----------------+
| exon_id           | int(10) unsigned     | NO   | PRI | NULL    | auto_increment |
| seq_region_id     | int(10) unsigned     | NO   | MUL | NULL    |                |
| seq_region_start  | int(10) unsigned     | NO   |     | NULL    |                |
| seq_region_end    | int(10) unsigned     | NO   |     | NULL    |                |
| seq_region_strand | tinyint(2)           | NO   |     | NULL    |                |
| phase             | tinyint(2)           | NO   |     | NULL    |                |
| end_phase         | tinyint(2)           | NO   |     | NULL    |                |
| is_current        | tinyint(1)           | NO   |     | 1       |                |
| is_constitutive   | tinyint(1)           | NO   |     | 0       |                |
| stable_id         | varchar(128)         | YES  | MUL | NULL    |                |
| version           | smallint(5) unsigned | YES  |     | NULL    |                |
| created_date      | datetime             | YES  |     | NULL    |                |
| modified_date     | datetime             | YES  |     | NULL    |                |
+-------------------+----------------------+------+-----+---------+----------------+
13 rows in set (0.06 sec)
```
## Assignment 3

> How many genes are registred for human? Make a breakdown based on the column "biotype" by using the GROUP BY directive.

```sh
 mysql -u anonymous -h ensembldb.ensembl.org -P 3306 homo_sapiens_core_90_38
```

```sh
 mysql> SELECT COUNT(*) FROM gene;
```

```sh
 +----------+
| COUNT(*) |
+----------+
|    64661 |
+----------+
```

```sh
mysql> SELECT biotype, COUNT(*) AS X
    -> FROM gene
    -> GROUP BY biotype ORDER BY X;
```

```sh
 +------------------------------------+----------+
| biotype                            | COUNT(*) |
+------------------------------------+----------+
| 3prime_overlapping_ncRNA           |       31 |
| antisense_RNA                      |     5718 |
| bidirectional_promoter_lncRNA      |       19 |
| IG_C_gene                          |       23 |
| IG_C_pseudogene                    |       11 |
| IG_D_gene                          |       64 |
| IG_J_gene                          |       24 |
| IG_J_pseudogene                    |        6 |
| IG_pseudogene                      |        1 |
| IG_V_gene                          |      227 |
| IG_V_pseudogene                    |      290 |
| lincRNA                            |     7821 |
| LRG_gene                           |      694 |
| macro_lncRNA                       |        1 |
| miRNA                              |     1890 |
| misc_RNA                           |     2390 |
| Mt_rRNA                            |        2 |
| Mt_tRNA                            |       22 |
| non_coding                         |        3 |
| polymorphic_pseudogene             |       90 |
| processed_pseudogene               |    10803 |
| processed_transcript               |      860 |
| protein_coding                     |    22375 |
| pseudogene                         |       40 |
| ribozyme                           |        8 |
| rRNA                               |      569 |
| scaRNA                             |       52 |
| scRNA                              |        1 |
| sense_intronic                     |      932 |
| sense_overlapping                  |      192 |
| snoRNA                             |     1006 |
| snRNA                              |     2053 |
| sRNA                               |        6 |
| TEC                                |     1093 |
| transcribed_processed_pseudogene   |      521 |
| transcribed_unitary_pseudogene     |      114 |
| transcribed_unprocessed_pseudogene |      974 |
| translated_processed_pseudogene    |        2 |
| TR_C_gene                          |        8 |
| TR_D_gene                          |        5 |
| TR_J_gene                          |       93 |
| TR_J_pseudogene                    |        4 |
| TR_V_gene                          |      161 |
| TR_V_pseudogene                    |       43 |
| unitary_pseudogene                 |       99 |
| unprocessed_pseudogene             |     3319 |
| vaultRNA                           |        1 |
+------------------------------------+----------+
```
## Assignment 4

> How many processed pseudogenes have a non-empty description string? 

```sh
mysql> SELECT COUNT(*) FROM gene WHERE biotype = 'processed_pseudogene' AND description IS NOT NULL;
```

```sh
+----------+
| COUNT(*) |
+----------+
|     5283 |
+----------+
```

## Assignment 5

> How many transcripts are associated with the two breast-cancer associated genes BRCA1 (ENSG00000012048) and BRCA2 (ENSG00000139618)? Your solution is supposed to be written as one SQL query. 

```sh
mysql> mysql> SELECT gene_id, description FROM gene WHERE description LIKE "%BRCA1%" OR description  LIKE "%BRCA2%" GROUP BY gene_id;
```


```sh
+---------+-------------------------------------------------------------------------------------------+
| gene_id | description                                                                               |
+---------+-------------------------------------------------------------------------------------------+
|  131115 | BRCA2, DNA repair associated [Source:HGNC Symbol;Acc:HGNC:1101]                           |
|  133548 | BRCA1 associated ATM activator 1 [Source:HGNC Symbol;Acc:HGNC:21701]                      |
|  134203 | BRCA1 associated protein [Source:HGNC Symbol;Acc:HGNC:1099]                               |
|  145208 | BRISC and BRCA1 A complex member 2 [Source:HGNC Symbol;Acc:HGNC:1106]                     |
|  154251 | BRCA1/BRCA2-containing complex subunit 3 pseudogene 1 [Source:HGNC Symbol;Acc:HGNC:51444] |
|  155145 | BRCA2 and CDKN1A interacting protein [Source:HGNC Symbol;Acc:HGNC:978]                    |
|  164395 | BRCA1 interacting protein C-terminal helicase 1 [Source:HGNC Symbol;Acc:HGNC:20473]       |
|  175918 | abraxas 1, BRCA1 A complex subunit [Source:HGNC Symbol;Acc:HGNC:25829]                    |
|  177755 | neighbor of BRCA1 gene 2 (non-protein coding) [Source:HGNC Symbol;Acc:HGNC:20691]         |
|  177770 | BRCA1, DNA repair associated [Source:HGNC Symbol;Acc:HGNC:1100]                           |
|  178593 | BRISC and BRCA1 A complex member 1 [Source:HGNC Symbol;Acc:HGNC:25008]                    |
|  178870 | BRCA1/BRCA2-containing complex subunit 3 [Source:HGNC Symbol;Acc:HGNC:24185]              |
|  178936 | BRCA1 associated protein 1 [Source:HGNC Symbol;Acc:HGNC:950]                              |
|  180323 | BRCA1 associated RING domain 1 [Source:HGNC Symbol;Acc:HGNC:952]                          |
|  181928 | partner and localizer of BRCA2 [Source:HGNC Symbol;Acc:HGNC:26144]                        |
|  182195 | EMSY, BRCA2 interacting transcriptional repressor [Source:HGNC Symbol;Acc:HGNC:18071]     |
|  193469 | BRCA1, DNA repair associated [Source:HGNC Symbol;Acc:HGNC:1100]                           |
|  193470 | BRCA2, DNA repair associated [Source:HGNC Symbol;Acc:HGNC:1101]                           |
|  193478 | BRCA1 interacting protein C-terminal helicase 1 [Source:HGNC Symbol;Acc:HGNC:20473]       |
|  193483 | partner and localizer of BRCA2 [Source:HGNC Symbol;Acc:HGNC:26144]                        |
|  193698 | BRCA1 associated protein 1 [Source:HGNC Symbol;Acc:HGNC:950]                              |
+---------+-------------------------------------------------------------------------------------------+
21 rows in set (0.09 sec)
```

```sh
mysql> SELECT gene_id FROM gene WHERE description LIKE "%BRCA1%" OR description  LIKE "%BRCA2%";
```


```sh
+---------+
| gene_id |
+---------+
|  177755 |
|  178593 |
|  180323 |
|  178870 |
|  178936 |
|  181928 |
|  182195 |
|  177770 |
|  175918 |
|  155145 |
|  154251 |
|  164395 |
|  145208 |
|  131115 |
|  133548 |
|  134203 |
|  193469 |
|  193470 |
|  193478 |
|  193483 |
|  193698 |
+---------+
21 rows in set (0.09 sec)
```


```sh
mysql> SELECT gene_id, COUNT(*) FROM gene WHERE description LIKE "%BRCA1%" OR description  LIKE "%BRCA2%";
```

```sh
+---------+----------+
| gene_id | COUNT(*) |
+---------+----------+
|  177755 |       21 |
+---------+----------+
```

```sh
mysql> select gene.gene_id, transcript.gene_id, transcript_id from gene, transcript
    -> WHERE gene.description LIKE "%BRCA1%" OR gene.description  LIKE "%BRCA2%" GROUP BY gene.description                                     -> AND gene.gene_id = transcript.gene_id; 
```

```sh
mysql> select tr.gene_id, COUNT(*) from gene 
    -> join transcript as tr on tr.gene_id = gene.gene_id 
    -> where gene.description like "%BRCA1%" or gene.description like "%BRCA2%" GROUP BY tr.gene_id;
```

```sh
+---------+----------+
| gene_id | COUNT(*) |
+---------+----------+
|  131115 |        7 |
|  133548 |        6 |
|  134203 |        3 |
|  145208 |       11 |
|  154251 |        1 |
|  155145 |        5 |
|  164395 |        6 |
|  175918 |        9 |
|  177755 |        4 |
|  177770 |       30 |
|  178593 |       18 |
|  178870 |       10 |
|  178936 |       11 |
|  180323 |       14 |
|  181928 |        6 |
|  182195 |       18 |
|  193469 |        1 |
|  193470 |        1 |
|  193478 |        1 |
|  193483 |        1 |
|  193698 |        1 |
+---------+----------+
21 rows in set (0.11 sec)
```


```sh
mysql> SELECT COUNT(*) from gene
    -> join transcript as tr on tr.gene_id = gene.gene_id
    -> where gene.description like "%BRCA1%" or gene.description like "%BRCA2%";
```


```sh
+----------+
| COUNT(*) |
+----------+
|      164 |
+----------+
1 row in set (0.09 sec)
```
