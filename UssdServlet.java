import java.io.IOException;
import javax.servlet.ServletException;
import javax.servlet.annotation.WebServlet;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;

@WebServlet("/ussd")
public class UssdServlet extends HttpServlet {
    @Override
    protected void doPost(HttpServletRequest request, HttpServletResponse response)
            throws ServletException, IOException {

        String sessionId   = request.getParameter("sessionId");
        String serviceCode = request.getParameter("serviceCode");
        String phoneNumber = request.getParameter("phoneNumber");
        String text        = request.getParameter("text");

        String ussdResponse;

        // First screen (*149*01#)
        if (text == null || text.isEmpty()) {
            ussdResponse = "CON Welcome to Vodacom\n"
                         + "1. Buy Data\n"
                         + "2. Check Balance\n"
                         + "3. Customer Care";
        }

        // Buy Data
        else if (text.equals("1")) {
            ussdResponse = "CON Buy Data\n"
                         + "1. Daily Bundle\n"
                         + "2. Weekly Bundle";
        }

        // Check Balance
        else if (text.equals("2")) {
            ussdResponse = "END Your balance is 25.50 MZN";
        }

        // Customer Care
        else if (text.equals("3")) {
            ussdResponse = "END Call 100 for customer care";
        }

        // Invalid option
        else {
            ussdResponse = "END Invalid option. Please try again.";
        }

        response.setContentType("text/plain");
        response.getWriter().write(ussdResponse);
    }
}