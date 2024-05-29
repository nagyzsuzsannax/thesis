from typing import List

def get_basic_operations_explanation()->List[str]:
    explanation_operations_block_1="""\nA mátrixok összeadása és kivonása csak azonos méretű mátrixok esetében végezhető el.\nAzaz, ha van két mxn méretű A és B mátrixunk, akkor összeadhatjuk és kivonhatjuk őket. \n\nHa van két A és B mátrixunk, ahol A𝑖𝑗​ és B𝑖𝑗 az A és B mátrixok i-edik sorának és j-edik oszlopának elemei, akkor az összeadásuk eredményeképp kapott C mátrix C𝑖𝑗 elemei a következőképpen számíthatók ki:"""
    explanation_operations_block_2="""Abban az esetben pedig ha kivonásra kerül az A mátrixból a B mátrix, a különbségük a következőképp áll elő:"""
    explanation_operations_block_3="""A mátrix szorzás esetében az első mátrix oszlopainak száma meg kell egyezzen a második mátrix sorainak számával. \nTehát, ha az A mátrix mérete mxn és a B mátrix mérete nxp, akkor az AxB szorzatuk egy mxp méretű C mátrix lesz, ahol minden C𝑖𝑗eleme a következő képlettel számítható ki: """
    return [explanation_operations_block_1,explanation_operations_block_2,explanation_operations_block_3]

def get_inverse_explanation()->List[str]:
    explanation_inverse_block_1="""\nEgy A négyzetes mátrix inverze, jelölt az a különleges mátrix, amelyet az A mátrixszal szorozva az egységmátrixot (identitásmátrixot) kapjuk, azaz:"""
    explanation_inverse_block_2="""A mátrixok inverze akkor létezik, ha mátrix nem szinguláris, azaz a determinánsa nem nulla."""
    explanation_inverse_block_3="""Az inverz mátrix meghatározásának egyik módszere, amit ez az alkalmazás is használ, a Gauss-elimináció, amely során a mátrixot és egy vele egy méretű egységmátrixot együtt alakítunk át. A Gauss-elimináció segítségével az eredeti mátrixot fokozatosan egységmátrixszá formáljuk, miközben a mellette lévő egységmátrix átalakul és az A mátrix inverzévé válik."""
    return [explanation_inverse_block_1,explanation_inverse_block_2,explanation_inverse_block_3]

def get_determinant_explanation()->List[str]:
    explanation_determanint_block_1="""\nA determináns egy számérték, amely egy négyzetes mátrixhoz van rendelve és jelentős információkat hordoz a mátrix tulajdonságairól. A determináns segítségével megállapítható egy mátrix invertálhatósága, hiszen egy mátrix akkor és csak akkor invertálható, ha a determinánsa nem nulla. Emellett a determináns szerepet játszik a mátrix sajátértékeinek kiszámításában, geometriai transzformációkban és a lineáris egyenletrendszerek megoldhatóságának vizsgálatában is. """
    explanation_determanint_block_2="""A determinánst számos módszerrel ki lehet számolni, köztük a Laplace-féle kifejtési tétellel:"""
    explanation_determanint_block_3="""Az LU-felbontás egy általános módszer determináns számítására, melyet ez a program is alkalmaz. Az A mátrix determinánsa, ha A=LU az LU-felbontás eredménye, kiszámítható az U mátrix diagonális elemeinek szorzataként. Ez azért lehetséges, mert az alsó háromszögű mátrixok determinánsa mindig a diagonális elemeik szorzata, és mivel az L mátrix diagonális elemei 1-ek, így a determináns nem változik a felbontás alkalmazásával:"""
    return [explanation_determanint_block_1,explanation_determanint_block_2,explanation_determanint_block_3]

def get_eigenvalues_explanation()->List[str]:           
    explanation_eigenvalues_block_1="""\nEgy mátrix sajátértékei olyan speciális skalárok, amelyek meghatározhatók a mátrixhoz kapcsolódó sajátérték-egyenlet megoldásával."""
    explanation_eigenvalues_block_2="""\nA sajátérték-egyenlet megoldása során a karakterisztikus polinom gyökeit számítjuk ki, és ezek a gyökök a mátrix sajátértékei:"""
    explanation_eigenvalues_block_3="""A QR-felbontással történő sajátértékszámítás egy iteratív módszer, amely a mátrixok sajátértékeit közelíti meg. \n\nEzt a módszert gyakran alkalmazzák nagy méretű mátrixok sajátértékeinek meghatározására, mivel hatékony és viszonylag stabil. Az alábbi iteráció ismétlésével a mátrix diagonális elemei konvergálnak a sajátértékekhez:"""
    return [explanation_eigenvalues_block_1, explanation_eigenvalues_block_2,explanation_eigenvalues_block_3]

def get_explanation_QR()->List[str]:
    explanation_QR_block_1="""\nA QR-felbontás egy fontos numerikus eljárás a lineáris algebrában, amely egy adott mátrixot két komponensre bont: egy ortogonális Q mátrixra és egy felső háromszög R mátrixra. \n\nEz a módszer széles körben használatos többek között lineáris egyenletrendszerek megoldására, a legkisebb négyzetek problémák kezelésére, valamint a mátrixok sajátértékeinek és sajátvektorainak meghatározására. A egy mxn mátrix, és a következőképp kerül felbontásra Q és R mátrixokra:"""
    explanation_QR_block_2="""ahol Q egy ortognális mátrix, R pedig egy felső háromszög mátrix."""
    explanation_QR_block_3="""\nA QR-felbontás egyik gyakori előállítási módja a Gram-Schmidt ortogonalizáció. A felbontás elvégzéséhez Gram-Schmidt ortogonalizációt végzünk el. \n\nElőször ortogonalizáljuk az A mátrix oszlopait a Gram-Schmidt módszer segítségével, hogy létrehozzuk az Q ortogonális mátrixot, majd a mátrixok szorzataiból kiszámítjuk az R felső háromszög mátrixot."""
    return [explanation_QR_block_1,explanation_QR_block_2,explanation_QR_block_3]
    
def get_explanation_LU()->List[str]:  
    explanation_LU_block_1="""\nAz LU-felbontás egy matematikai eljárás, amely egy adott A négyzetes mátrixot alsó háromszögű L és felső háromszögű U mátrixok szorzatára bont:"""
    explanation_LU_block_2="""\n Az L és U mátrixokat lépésről lépésre számoljuk Gauss eliminációval, miután az L-t egységmátrixra, az U-t pedig az A mátrixra inicializáltuk. Az L mátrix diagonális elemei az 1-esek maradnak, míg az U mátrix elemei az A mátrix felső háromszögének elemei lesznek. \n\nEz a módszer alapvetően hasznos a lineáris egyenletrendszerek megoldásában, a mátrixok determinánsának és inverzének gyors kiszámításában."""
    explanation_LU_block_3="""\nFontos megjegyezni, hogy csak nem szinguláris mátrixokon elvégezhető művelet."""
    return [explanation_LU_block_1,explanation_LU_block_2,explanation_LU_block_3]

def get_explanation_Cholesky()->List[str]:
    explanation_Cholesky_block_1="""\nA Cholesky-felbontás egy speciális típusa az LU-felbontásnak, amelyet szimmetrikus és pozitív definit mátrixok felbontására használnak. \n\nEz a módszer egy adott A mátrixot egy alsó háromszögű L mátrix és annak transzponáltjának szorzatára bontja:"""
    explanation_Cholesky_block_2="""A Cholesky-felbontás előnye, hogy gyorsabb és stabilabb, mint az általános LU-felbontás, viszont csak szimmetrikus, pozitív definit mátrixok esetén alkalmazható. """
    explanation_Cholesky_block_3="""\nA Cholesky-felbontás csak fele annyi műveletet igényel, mint az általános LU-felbontás, mivel a szimmetria miatt csak az L mátrixot kell kiszámítani. """
    return [explanation_Cholesky_block_1,explanation_Cholesky_block_2,explanation_Cholesky_block_3]