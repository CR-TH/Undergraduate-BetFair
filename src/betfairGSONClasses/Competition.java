package betfairGSONClasses;

/**
 * This class is used for GSON serialisation
 * CLASS TAKEN FROM BETFAIR source: https://github.com/betfair/API-NG-sample-code/tree/master/java/ng
 * @author Betfair
 */
public class Competition
{
	private String id;
	private String name;

	public String getId()
	{
		return id;
	}

	public void setId(String id)
	{
		this.id = id;
	}

	public String getName()
	{
		return name;
	}

	public void setName(String name)
	{
		this.name = name;
	}

	public String toString()
	{
		return "{" + "" + "id=" + getId() + "," + "name=" + getName() + "}";
	}
}