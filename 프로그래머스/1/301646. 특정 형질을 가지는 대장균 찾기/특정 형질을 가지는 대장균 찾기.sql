-- 코드를 작성해주세요
SELECT COUNT(ID) AS COUNT
FROM ECOLI_DATA
WHERE (GENOTYPE & 4 = 4 OR GENOTYPE & 1 = 1)  AND GENOTYPE & 2 = 0