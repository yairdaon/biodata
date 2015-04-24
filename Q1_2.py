import sqlite3
import optparse

#----------------------------------------------------------------------
def findparent(c,son):
    """
    looking for parent use the recursion
    """
    c.execute("SELECT parent_id,genus FROM species WHERE id=?;", (son,))
    parent=c.fetchall()
    if (len(parent)!=0):
        sonname=parent[0][1]
        parent=parent[0][0]
        print sonname+"|",
        if (parent!=None):
            findparent(c, parent)
    
if __name__=="__main__":
    parser=optparse.OptionParser()
    parser.add_option("-D",dest="sqlite",default="",help="full pathname of sqlite file")    
    parser.add_option("-Q",dest="query",default="",help="query name")
    (options,args)=parser.parse_args()
    database=options.sqlite    
    query=options.query
    
    conn=sqlite3.connect(database)
    c = conn.cursor()
    c.execute('select DISTINCT species.id,species.parent_id,species.genus from term JOIN association on term.id=association.term_id JOIN gene_product ON association.gene_product_id=gene_product.id JOIN species ON gene_product.species_id=species.id where term.name=?', (query,));
    sons=c.fetchall()
    for son in sons:
        findparent(c, son[1])
        print
    