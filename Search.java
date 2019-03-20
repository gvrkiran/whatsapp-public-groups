/*
Edgard Chammas - 25/07/2018

Whatsapp database mediaKey dump
This tool will dump the mediakey needed to decrypt any media file (image, audio, etc)

COMPILE: javac Search.java
RUN: java -classpath ".:PATH_TO_SQLITE_JDBC_JAR/sqlite-jdbc-3.8.6.jar" Search msgstore.db
*/

import java.io.File;
import java.io.FileInputStream;
import java.io.FileNotFoundException;
import java.io.IOException;
import java.io.ByteArrayInputStream;
import java.io.ObjectInputStream;
import java.io.ObjectInput;

import java.sql.DriverManager;
import java.sql.Connection;
import java.sql.ResultSet;
import java.sql.SQLException;
import java.sql.Statement;

import com.whatsapp.MediaData;

public class Search {

    public static Connection connect(String path) {
        String url = "jdbc:sqlite:"+path;
        Connection conn = null;
        try { conn = DriverManager.getConnection(url);
        } catch (SQLException e) { System.out.println(e.getMessage()); }
        return conn;
    }

	public static String byteArrayToHexString(final byte[] b) {
		final StringBuffer sb = new StringBuffer(b.length * 2);

		for (final byte element : b) {
			final int v = element & 0xff;
			if (v < 16) {
				sb.append('0');
			}
			sb.append(Integer.toHexString(v));
		}
		return sb.toString().toUpperCase();
	}

	public static void main(String args[]) throws ClassNotFoundException {

        Class.forName("org.sqlite.JDBC");

//        String sql = "SELECT media_url, media_mime_type, thumb_image FROM messages";
        String sql = "SELECT data, media_url, media_mime_type, thumb_image, media_wa_type, media_enc_hash, media_hash, key_id, key_remote_jid,  remote_resource, timestamp, forwarded, recipient_count from messages";
        
        try (Connection conn = connect(args[0]);
             Statement stmt  = conn.createStatement();
             ResultSet rs    = stmt.executeQuery(sql)){
            
            while (rs.next()) {
		    	    String data = rs.getString("data");
			    String media_url = rs.getString("media_url");
			    String media_mime_type = rs.getString("media_mime_type");
			    byte[] thumb_image = rs.getBytes("thumb_image");

                if (media_url != null && media_mime_type != null) {

                    if(! media_url.substring(media_url.length() - 3).equals("enc")) continue;

                    System.out.print(media_url + " " + media_mime_type + " ");

				    try {
					    ByteArrayInputStream bis = new ByteArrayInputStream(thumb_image);
					    ObjectInput in = new ObjectInputStream(bis);
					    MediaData media = (MediaData) in.readObject();
					    System.out.println(byteArrayToHexString(media.mediaKey));
				    }
				    catch (IOException ioe) { System.out.println(ioe.getMessage()); }
				    catch (ClassNotFoundException e) { System.out.println(e.getMessage()); }
			    }
            }

        } catch (SQLException e) { System.out.println(e.getMessage()); }
	}
}
