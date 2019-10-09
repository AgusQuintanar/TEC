public class Preferences {
	private boolean shareInfo;
	private static Preferences uniquePreferences = null;
	
	private Preferences() {
		this.shareInfo = false;
	}

	public void setShareInfo(boolean value){
		this.shareInfo = value;
	}

	public static Preferences getInstance() {
		return uniquePreferences == null ? uniquePreferences = new Preferences():uniquePreferences;
	}
	
	public String toString()
	{
		return "Application Preferences:\nShare information: " + this.shareInfo; 
	}
}
