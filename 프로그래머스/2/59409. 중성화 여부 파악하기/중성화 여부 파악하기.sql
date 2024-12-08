SELECT 
    ANIMAL_ID, 
    NAME, 
    IF(SEX_UPON_INTAKE LIKE 'Neutered Male' 
       OR SEX_UPON_INTAKE LIKE 'Spayed Female'
      , "O", "X") AS "중성화"
FROM ANIMAL_INS
ORDER BY ANIMAL_ID;