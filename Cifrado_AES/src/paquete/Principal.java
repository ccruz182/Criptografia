package paquete;

import java.io.File;
import javax.crypto.Cipher;
import utilerias.UtileriasCifrado;

/**
 *
 * @author cesar
 */
public class Principal {

  public static void main(String[] args) {
    String llave = "1234567890123456";
    File archivoOriginal = new File("original.pdf");
    File archivoCifrado = new File("cifrado.pdf");
    File archivoRecuperado = new File("recuperado.pdf");
    
    UtileriasCifrado utilerias = new UtileriasCifrado();
    utilerias.setCifrado("AES");
    // utilerias.setModoCifrado(Cipher.ENCRYPT_MODE);
    utilerias.setModoCifrado(Cipher.DECRYPT_MODE);
    
    // utilerias.procesamiento(llave, archivoOriginal, archivoCifrado);
    utilerias.procesamiento(llave, archivoCifrado, archivoRecuperado);
  }

}
