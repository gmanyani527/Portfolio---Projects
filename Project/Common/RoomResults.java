package Project.Common;

import java.util.ArrayList;
import java.util.List;

public class RoomResults extends Payload {
    private List<String> rooms = new ArrayList<String>();

    public List<String> getRooms() {
        return rooms;
    }

    public void setRooms(List<String> rooms) {
        this.rooms = rooms;
    }
}
