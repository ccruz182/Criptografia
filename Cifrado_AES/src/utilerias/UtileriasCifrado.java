package utilerias;

import java.io.File;
import java.io.FileInputStream;
import java.io.FileOutputStream;
import java.io.IOException;
import java.security.InvalidKeyException;
import java.security.Key;
import java.security.NoSuchAlgorithmException;
import javax.crypto.BadPaddingException;
import javax.crypto.Cipher;
import javax.crypto.IllegalBlockSizeException;
import javax.crypto.NoSuchPaddingException;
import javax.crypto.spec.SecretKeySpec;

/**
 *
 * @author cesar
 */
public class UtileriasCifrado {

  private String cifrado;
  private int modoCifrado;

  public void procesamiento(String llave, File archivo1, File outputFile) {
    try {
      Key secretKey = new SecretKeySpec(llave.getBytes(), this.cifrado);
      Cipher cipher = Cipher.getInstance(this.cifrado);
      cipher.init(this.modoCifrado, secretKey);

      FileInputStream inputStream = new FileInputStream(archivo1);
      byte[] inputBytes = new byte[(int) archivo1.length()];
      inputStream.read(inputBytes);

      byte[] outputBytes = cipher.doFinal(inputBytes);

      FileOutputStream outputStream = new FileOutputStream(outputFile);
      outputStream.write(outputBytes);

      inputStream.close();
      outputStream.close();

    } catch (NoSuchPaddingException | NoSuchAlgorithmException
            | InvalidKeyException | BadPaddingException
            | IllegalBlockSizeException | IOException e) {
      e.printStackTrace();
    }
  }

  public String getCifrado() {
    return cifrado;
  }

  public void setCifrado(String cifrado) {
    this.cifrado = cifrado;
  }

  public int getModoCifrado() {
    return modoCifrado;
  }

  public void setModoCifrado(int modoCifrado) {
    this.modoCifrado = modoCifrado;
  }
  
  

}
