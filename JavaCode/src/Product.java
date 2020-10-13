package src;

public class Product {

    String name = "";
    int qty = 0;
    
    public void setName(String string) {
        this.name = string;
	}

	public void setQty(int i) {
        this.qty = i;
    }
    public String getName(){
        return this.name;
    }
    public int getQty(){
        return this.qty;
    }

}
