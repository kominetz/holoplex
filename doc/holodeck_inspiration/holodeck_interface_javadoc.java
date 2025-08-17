
/**
 * Star Trek Holodeck Programming Interface
 * 
 * The primary interface for holographic simulation programming and control.
 * Provides methods for program lifecycle management, character creation,
 * safety protocol control, and environmental simulation.
 * 
 * @author Starfleet Command
 * @version 24th Century
 * @since TNG Season 1
 */
public interface HolodeckInterface {

    // ==================== CORE PROGRAM CONTROL ====================

    /**
     * Initiates execution of a specified holographic program.
     * 
     * @param programName the identifier of the program to execute
     * @return ProgramStatus indicating success or failure
     * @throws HolodeckException if program not found or system unavailable
     * @see #endProgram()
     * @see #freezeProgram()
     * 
     * Usage: "Computer, run program"
     */
    public ProgramStatus runProgram(String programName);

    /**
     * Terminates the currently active holographic program and returns
     * holodeck to idle state.
     * 
     * @return ProgramStatus indicating termination success
     * @see #runProgram(String)
     * @see #freezeProgram()
     * 
     * Usage: "Computer, end program"
     */
    public ProgramStatus endProgram();

    /**
     * Temporarily suspends the current program execution while maintaining
     * all program state and character positions.
     * 
     * @return ProgramStatus indicating freeze success
     * @see #runProgram(String)
     * @see #endProgram()
     * 
     * Usage: "Computer, freeze program"
     */
    public ProgramStatus freezeProgram();

    /**
     * Permanently removes a program from holodeck memory storage.
     * 
     * @param programName the identifier of the program to delete
     * @return boolean true if deletion successful
     * @throws SecurityException if insufficient privileges
     * 
     * Usage: "Computer, delete program"
     */
    public boolean deleteProgram(String programName);

    /**
     * Preserves current program state to permanent storage for future use.
     * 
     * @param programName the identifier for the saved program
     * @return boolean true if save successful
     * @throws StorageException if insufficient memory
     * 
     * Usage: "Computer, save program"
     */
    public boolean saveProgram(String programName);

    // ==================== INTERFACE ACCESS ====================

    /**
     * Summons the holographic control interface panel within the simulation.
     * The arch provides visual access to program controls and system status.
     * 
     * @return ArchInterface the control panel object
     * @see #exit()
     * 
     * Usage: "Computer, arch"
     */
    public ArchInterface arch();

    /**
     * Reveals the physical holodeck exit and removes environmental simulation
     * barriers, allowing users to leave the holographic environment.
     * 
     * @return ExitStatus indicating door accessibility
     * @see #arch()
     * 
     * Usage: "Computer, exit"
     */
    public ExitStatus exit();

    // ==================== SAFETY SYSTEMS ====================

    /**
     * Disables holodeck safety protocols, allowing potentially dangerous
     * interactions within the simulation. USE WITH EXTREME CAUTION.
     * 
     * @param authorizationCode required security clearance
     * @return SafetyStatus indicating protocol state
     * @throws SecurityException if insufficient authorization
     * @see #enableSafetyProtocols()
     * 
     * Usage: "Computer, disable safety protocols"
     */
    public SafetyStatus disableSafetyProtocols(String authorizationCode);

    /**
     * Enables holodeck safety protocols, preventing physical harm to users
     * within the holographic simulation.
     * 
     * @return SafetyStatus indicating protocol state
     * @see #disableSafetyProtocols(String)
     * 
     * Usage: "Computer, enable safety protocols"
     */
    public SafetyStatus enableSafetyProtocols();

    // ==================== CHARACTER MANAGEMENT ====================

    /**
     * Creates a new holographic character within the current program
     * based on specified parameters.
     * 
     * @param characterName unique identifier for the character
     * @param parameters CharacterParameters defining appearance and behavior
     * @return HolographicCharacter the created character object
     * @throws CreationException if parameters invalid
     * @see #modifyCharacter(String, CharacterParameters)
     * @see #deleteCharacter(String)
     * 
     * Usage: "Computer, create character"
     */
    public HolographicCharacter createCharacter(String characterName, CharacterParameters parameters);

    /**
     * Modifies an existing holographic character's parameters, including
     * appearance, personality traits, and behavioral patterns.
     * 
     * @param characterName the identifier of the character to modify
     * @param newParameters updated CharacterParameters
     * @return boolean true if modification successful
     * @see #createCharacter(String, CharacterParameters)
     * 
     * Usage: "Computer, modify character"
     */
    public boolean modifyCharacter(String characterName, CharacterParameters newParameters);

    /**
     * Removes a holographic character from the current program.
     * 
     * @param characterName the identifier of the character to remove
     * @return boolean true if deletion successful
     * @see #createCharacter(String, CharacterParameters)
     * 
     * Usage: "Computer, delete character"
     */
    public boolean deleteCharacter(String characterName);

    // ==================== PROGRAM TYPES AND MANAGEMENT ====================

    /**
     * Creates a new holographic program with specified parameters and
     * environmental settings.
     * 
     * @param programType the type of program (HOLONOVEL, TRAINING, RECREATIONAL)
     * @param programName unique identifier for the program
     * @param parameters ProgramParameters defining environment and rules
     * @return HolographicProgram the created program object
     * @see ProgramType
     * 
     * Usage: "Computer, create program"
     */
    public HolographicProgram createProgram(ProgramType programType, String programName, ProgramParameters parameters);

    /**
     * Recreates historical figures, locations, or scenarios based on
     * database records and historical archives.
     * 
     * @param subject the historical entity to recreate
     * @param timeperiod the specific era or date for accuracy
     * @return HolographicRecreation the recreated historical simulation
     * 
     * Usage: "Computer, recreate [historical subject]"
     */
    public HolographicRecreation recreate(String subject, TimePeriod timeperiod);

    /**
     * Generates environmental or technical simulations for analysis,
     * training, or problem-solving purposes.
     * 
     * @param simulationType the type of simulation required
     * @param parameters environmental or technical specifications
     * @return Simulation the generated simulation environment
     * 
     * Usage: "Computer, simulate [environment/scenario]"
     */
    public Simulation simulate(SimulationType simulationType, SimulationParameters parameters);
}

/**
 * Emergency Medical Hologram Interface
 * 
 * Specialized interface for EMH program management and medical holographic
 * systems. Extends standard holographic programming with medical-specific
 * functionality.
 * 
 * @author Dr. Lewis Zimmerman
 * @version Mark I through VII
 * @since Voyager
 */
public interface EMHInterface extends HolographicCharacter {

    /**
     * Activates the Emergency Medical Hologram program and initializes
     * medical diagnostic systems.
     * 
     * @return ActivationStatus indicating EMH readiness
     * @see #deactivateEMH()
     * 
     * Usage: "Computer, activate EMH"
     * Response: "Please state the nature of the medical emergency"
     */
    public ActivationStatus activateEMH();

    /**
     * Deactivates the Emergency Medical Hologram and stores program state.
     * 
     * @return DeactivationStatus indicating shutdown success
     * @see #activateEMH()
     * 
     * Usage: "Computer, deactivate EMH"
     */
    public DeactivationStatus deactivateEMH();

    /**
     * Transfers EMH program to specified location with compatible
     * holographic projection systems.
     * 
     * @param destination target location with holographic emitters
     * @return TransferStatus indicating transfer success
     * @throws TransferException if destination incompatible
     * 
     * Usage: "Computer, transfer EMH to [location]"
     */
    public TransferStatus transferEMH(Location destination);

    /**
     * Standard EMH activation greeting and status inquiry.
     * 
     * @return String the nature of the reported medical emergency
     * 
     * Standard Response: "Please state the nature of the medical emergency"
     */
    public String requestEmergencyNature();
}

/**
 * Holographic Character Entity
 * 
 * Represents an individual holographic character with behavioral patterns,
 * interaction capabilities, and potential for autonomous development.
 */
public class HolographicCharacter {

    /** Character's unique identifier within the program */
    private String characterName;

    /** Behavioral and personality parameters */
    private CharacterParameters parameters;

    /** Current awareness level of holographic nature */
    private AwarenessLevel selfAwareness;

    /** Interactive capability level */
    private InteractivityLevel interactive;

    /** Autonomous behavior development capability */
    private boolean autonomous;

    /** Character sentience status */
    private SentienceLevel sentient;

    /**
     * Returns the character's current awareness of their holographic nature.
     * 
     * @return AwarenessLevel current self-awareness state
     */
    public AwarenessLevel getCharacterAwareness() {
        return this.selfAwareness;
    }

    /**
     * Updates character parameters including personality and behavior.
     * 
     * @param newParameters updated character specifications
     * @return boolean true if update successful
     */
    public boolean updateCharacterParameters(CharacterParameters newParameters) {
        // Implementation would update character behavior
        return true;
    }
}

/**
 * Holodeck Arch Interface
 * 
 * The primary visual control interface within holographic simulations.
 * Provides access to program controls and system status.
 */
public class ArchInterface {

    /** Visual control panel for program management */
    private ControlPanel controlPanel;

    /** Interface visibility state */
    private boolean visible;

    /**
     * Displays the arch control interface within the holographic environment.
     */
    public void displayArch() {
        this.visible = true;
    }

    /**
     * Hides the arch interface and returns to full simulation immersion.
     */
    public void hideArch() {
        this.visible = false;
    }
}

// ==================== ENUMS AND DATA TYPES ====================

/**
 * Program execution status indicators
 */
public enum ProgramStatus {
    RUNNING, TERMINATED, FROZEN, SUSPENDED, LOADING, ERROR
}

/**
 * Safety protocol states
 */
public enum SafetyStatus {
    ENABLED, DISABLED, PARTIAL, MALFUNCTION
}

/**
 * Character awareness levels
 */
public enum AwarenessLevel {
    NONE, LIMITED, PARTIAL, FULL_AWARENESS, TRANSCENDENT
}

/**
 * Character sentience development levels
 */
public enum SentienceLevel {
    NON_SENTIENT, RESPONSIVE, ADAPTIVE, SENTIENT, AUTONOMOUS
}

/**
 * Available program types
 */
public enum ProgramType {
    HOLONOVEL, TRAINING, RECREATIONAL, DIAGNOSTIC, HISTORICAL_RECREATION, SIMULATION
}
